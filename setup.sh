#!/bin/bash

# Create a virtual environment
python3.10 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt

echo "Virtual environment setup complete. Dependencies installed."
