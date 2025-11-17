# ENTSO‑E Transparency Platform — behavior and processing details

This page explains how the project interacts with the ENTSO‑E Transparency Platform, how requests are chunked, how timestamps are interpreted, and how missing data is handled for each supported document type. Use this page as the canonical reference for implementation details and for reproducing results.

Table of contents

- [Overview](#overview)
- [Request parameters and headers](#request-parameters-and-headers)
- [Time handling and timezone](#time-handling-and-timezone)
- [Chunking and pagination logic](#chunking-and-pagination-logic)
- [Parsing and timestamp mapping per document type](#parsing-and-timestamp-mapping-per-document-type)
  - [PRICE_DOCUMENT](#price_document)
  - [ACTUAL_GENERATION_PER_TYPE](#actual_generation_per_type)
  - [SYSTEM_TOTAL_LOAD](#system_total_load)
  - [WIND_AND_SOLAR_FORECAST](#wind_and_solar_forecast)
  - [AGGREGATED_ENERGY_DATA_REPORT](#aggregated_energy_data_report)
- [Gap filling strategies and examples](#gap-filling-strategies-and-examples)
- [Practical CLI examples and expected outcomes](#practical-cli-examples-and-expected-outcomes)
- [Notes and caveats](#notes-and-caveats)

<a id="overview"></a>
## Overview

The ENTSO‑E Transparency Platform provides electricity-related datasets (generation per type, prices, load, forecasts, aggregated reports) as XML documents. This project fetches those XML documents, parses them into pandas.DataFrame objects and applies deterministic post-processing to produce time-indexed tabular outputs.

<a id="request-parameters-and-headers"></a>
## Request parameters and headers

- Base URL: `https://web-api.tp.entsoe.eu/api`
- Authentication: `securityToken` query parameter (your API key).
- Common query parameters set by the client:
  - `documentType` — chosen from `DocumentType` enum.
  - `processType` — chosen from `ProcessType` enum (e.g. DAY_AHEAD, REALISED).
  - `in_Domain` — incoming bidding zone code (from `DomainType`).
  - `out_Domain` — outgoing bidding zone code (from `DomainType`).
  - `OutBiddingZone_Domain` — set by the client to the same value as `in_Domain` for requests (present in current implementation).
  - `periodStart` / `periodEnd` — formatted as `YYYYMMDDHH00`.

<a id="time-handling-and-timezone"></a>
## Time handling and timezone

- XML timestamps from ENTSO‑E are parsed with format `%Y-%m-%dT%H:%MZ`. The `Z` suffix denotes UTC.
- The library parses these timestamps into timezone-naive Python `datetime` objects representing UTC instants. The resulting DataFrame indices are timezone-naive; treat them as UTC.
- Consumers who require local time should convert the index explicitly (for example with `df.tz_localize('UTC').tz_convert('Europe/Oslo')`).

<a id="chunking-and-pagination-logic"></a>
## Chunking and pagination logic

- The client supports automatic chunking of long date ranges using the `max_period_days` parameter (default 30).
- If the requested date range length in days exceeds `max_period_days`, the `fetch_data` method splits the total range into sequential chunks of up to `max_period_days` days and calls itself recursively for each chunk. The returned DataFrames are concatenated in chronological order.
- Special handling for `PRICE_DOCUMENT`: the chunk end calculation uses `max_period_days - 1` when computing the chunk end and also applies an `end_date - 1 day` correction when taking the min with the requested end. This implements a slightly different inclusive/exclusive semantics for price documents; the code therefore ensures price requests do not inadvertently overlap or exceed permitted ranges. (If you rely on exact inclusive/exclusive boundaries, verify results for `PRICE_DOCUMENT` and adjust `max_period_days` accordingly.)
- Rate limiting: the client defines `REQUEST_DELAY = 0.5` seconds — callers should respect this and any API rate limits.

<a id="parsing-and-timestamp-mapping-per-document-type"></a>
## Parsing and timestamp mapping per document type

Important general note about positions and timestamps:
- ENTSO‑E `Point` elements include a 1-based `position` child. This project maps a point's timestamp to `start_date + position * interval_minutes`.
- That means the first reported value in a TimeSeries is assigned to `start + interval`, not to `start` itself. This is consistent across price and production parsers in the current implementation.

<a id="price_document"></a>
### PRICE_DOCUMENT

- Parser: `PriceDataParser`.
- Time mapping: for each `Point`, timestamp = `timeInterval.start + position * interval_minutes`.
- Gap-filling: after parsing the points into a DataFrame indexed by timestamp, the parser creates a complete index from `start + interval` to `end` with frequency equal to the resolution (e.g., 15 minutes). It then reindexes the parsed DataFrame and forward-fills missing values (`ffill`).
  - Implementation detail: the index is created with `pd.date_range(start=time_start + timedelta(minutes=interval), end=time_end, freq=f'{interval}min')` and `df.reindex(idx, method='ffill')` is used.
  - Effect: missing price values are filled with the most recent known price. If the first interval(s) are missing, they remain NaN (there is no backward fill before the first known value).

<a id="actual_generation_per_type"></a>
### ACTUAL_GENERATION_PER_TYPE

- Parser: `ProductionDataParser`.
- Time mapping: similar to prices — timestamps are `start + position * interval_minutes` for each `Point`.
- Aggregation: the parser aggregates `Quantity` by `(timestamp, PsrType)`, sums duplicates, then pivots to have `PsrType` values as columns.
- Gap-filling: after pivoting, the DataFrame uses `.fillna(0)` so missing combinations of timestamp and generation type are treated as zero production.
  - Effect: absent measurements for a particular `PsrType` at a timestamp are interpreted as 0 in the final table.

<a id="system_total_load"></a>
### SYSTEM_TOTAL_LOAD

- Parser registration: `SYSTEM_TOTAL_LOAD` is mapped to `TotalLoad` parser (implementation lives in parser_extensions).
- Behavior: follows general parsing rules; make sure to inspect `TotalLoad` parser for any specific timestamp offsets or fill strategies. Typical expected output is a single-column time series of total load.

<a id="wind_and_solar_forecast"></a>
### WIND_AND_SOLAR_FORECAST

- Currently routed to the `ProductionDataParser` implementation (shared logic), so timestamps and fill strategies follow the production rules (pivot + fillna(0)).

<a id="aggregated_energy_data_report"></a>
### AGGREGATED_ENERGY_DATA_REPORT

- Parser: `AggregatedEnergyDataDataParser` (registered in `DataParser`). This parser is intended for aggregated reports and may produce multiple columns. Check the parser implementation for specific semantics.

<a id="gap-filling-strategies-and-examples"></a>
## Gap filling strategies and examples

- Price documents: forward-fill (ffill) after reindexing to the expected regular timestamps. Useful when prices are updated intermittently but should be applied to every interval.
- Production and forecast documents: missing PSR types are filled with 0 after pivoting — this means absence of a reported value is interpreted as zero generation for that type at that timestamp.
- System load: depends on `TotalLoad` implementation; usually either ffill or numeric interpolation may be used — consult parser code if you rely on a specific method.

<a id="practical-cli-examples-and-expected-outcomes"></a>
## Practical CLI examples and expected outcomes

Below are the example invocations you provided and what the client will do for each. For brevity we assume `--start-date`/`--end-date` are inclusive date bounds used to build datetimes at midnight; the code converts them to `datetime` objects and then constructs `periodStart`/`periodEnd` in `YYYYMMDDHH00` format.

<a id="notes-and-caveats"></a>
## Notes and caveats

- Timezones: raw times are parsed as UTC (via the `Z` designator). The project returns timezone-naive timestamps representing UTC times. Convert explicitly if you need localized times.
- Inclusive/exclusive ranges: the code's chunking logic and the way `periodEnd` is computed differ slightly for price documents. If you need exact reproducibility at boundary dates, test with a small date range first and inspect generated `periodStart`/`periodEnd` values.
- Gap-filling implications:
  - Forward-fill for prices can carry a previous price across missing intervals — this is intended because price updates may be sparse but applicable for all intervals until the next update.
  - Filling missing production types with zeros assumes that absence of a reported value equals zero production — this matches common ENTSO‑E reporting, but verify against your quality requirements.
- Performance: large ranges produce many HTTP requests (one per chunk). Tune `--chunk_size` and be mindful of API rate limits and the `REQUEST_DELAY` pause between requests.

If you want, I can also:
- add small example XML snippets and show the parsed DataFrame for each document type,
- add unit-test style examples demonstrating gap-filling behavior,
- or create a small script that prints exact `periodStart`/`periodEnd` values for a given command so you can validate chunk boundaries before running the full fetch.

---

Navigation

- [Back to Index](index.md)
- [Usage (Quickstart)](usage.md)
- [API reference](api.md)
