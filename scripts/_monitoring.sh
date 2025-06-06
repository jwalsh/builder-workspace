#!/bin/bash

# Create the main monitoring directory
mkdir -p monitoring

# Create subdirectories
mkdir -p monitoring/prometheus
mkdir -p monitoring/grafana/dashboards
mkdir -p monitoring/grafana/datasources
mkdir -p monitoring/exporters
mkdir -p monitoring/scripts
mkdir -p monitoring/tests

# Create files
touch monitoring/docker-compose.yml
touch monitoring/prometheus/prometheus.yml
touch monitoring/prometheus/alerts.yml
touch monitoring/grafana/dashboards/overview.json
touch monitoring/grafana/dashboards/dora_metrics.json
touch monitoring/grafana/dashboards/slo_tracking.json
touch monitoring/grafana/datasources/prometheus.yml
touch monitoring/exporters/rfc_exporter.py
touch monitoring/exporters/implementation_exporter.py
touch monitoring/exporters/agent_performance_exporter.py
touch monitoring/scripts/setup_monitoring.sh
touch monitoring/scripts/update_dashboards.sh
touch monitoring/tests/test_exporters.py
touch monitoring/tests/test_metrics_simulator.py

echo "Monitoring directory structure and files created successfully."
