#!/bin/bash
echo "Creating virtual environment..."
python -m venv venv

echo "Activating virtual environment..."
source venv/Scripts/activate

echo "Installing requirements..."
pip install -r requirements.txt

echo "Running simulation..."
python -m src.main

echo "That's all folks!"
