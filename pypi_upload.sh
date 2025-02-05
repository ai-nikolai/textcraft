#!/bin/bash

# NOTE: you need to first install the package "twine" (e.g. pip3 install twine)

# Upload using twine and API token
TWINE_USERNAME="__token__" \
TWINE_PASSWORD="$PYPI_API_KEY" \
python3 -m twine upload dist/*
