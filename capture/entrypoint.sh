#!/bin/bash

# Create virtualenv
if [ ! -f venv/bin/activate ]; then 
    virtualenv -p python3 venv
fi

# Activate virtualenv
source venv/bin/activate

# Update libs
pip install -r requirements.txt

# Run Python code
python main.py

