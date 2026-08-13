# Makefile for Hyperion Framework
install:
    pip install -r requirements.txt
quickstart:
    python demo.py
test:
    pytest tests