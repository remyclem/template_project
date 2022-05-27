#!/bin/bash

##### Creation of a virtual environment
echo "Creation of a python virtual environment."
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Installation done."