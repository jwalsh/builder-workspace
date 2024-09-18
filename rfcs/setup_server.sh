#!/bin/bash

# Install dependencies
sudo apt update
sudo apt install -y python3 python3-venv python3-pip prometheus node_exporter grafana

# Set up Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Install Ollama
curl https://ollama.ai/install.sh | sh

# Start monitoring services
sudo systemctl start prometheus
sudo systemctl start node_exporter
sudo systemctl start grafana-server

# Run Project Manager
python project_manager.py
