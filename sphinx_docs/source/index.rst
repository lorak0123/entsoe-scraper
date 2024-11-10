Welcome to Entsoe API documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
   <other_module>  # Dodaj inne moduły tutaj, jeśli są

Installation
------------

To install the package, run:

.. code-block:: bash

   pip install entsoe_api

Usage

To use the package, run:

.. code-block:: python

   from entsoe_api.api import EntsoeAPI
   from entsoe_api.enums import DocumentType, ProcessType, DomainType, PsrType
   from datetime import datetime

   api = EntsoeAPI(api_key="YOUR_API_KEY")

   start_date = datetime(2022, 1, 1)
   end_date = datetime(2022, 1, 31)
   document_type = DocumentType.ACTUAL_GENERATION_PER_TYPE
   process_type = ProcessType.REALISED
   domain = DomainType.DE

   data = api.fetch_data(start_date, end_date, document_type, process_type, domain)
   data.to_csv("output.csv", index=False)

