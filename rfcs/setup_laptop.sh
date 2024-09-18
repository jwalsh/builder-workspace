#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
curl https://ollama.ai/install.sh | sh
python project_manager.py
