import logging

LOGGER = logging.getLogger("entsoe-api")
LOGGER.addHandler(logging.StreamHandler())
LOGGER.setLevel(logging.DEBUG)
