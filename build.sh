#!/usr/bin/env bash

# Upgrade pip first
python -m pip install --upgrade pip==25.0.1

# Then install your dependencies
pip install -r requirements.txt
