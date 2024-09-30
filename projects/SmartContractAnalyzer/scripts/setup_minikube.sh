#!/bin/bash

# Start Minikube
minikube start

# Enable ingress addon
minikube addons enable ingress

# Set up local Docker environment to use Minikube's Docker daemon
eval $(minikube docker-env)

# Build Docker images for each service
for service in frontend api-gateway smart-contract-parser analysis-engine legal-compliance vulnerability-scanner report-generator; do
  docker build -t smartcontractanalyzer/$service:latest ./$service
done

# Apply Kubernetes configurations
kubectl apply -f k8s/

# Wait for deployments to be ready
kubectl wait --for=condition=available --timeout=300s deployment --all

# Get Minikube IP
minikube_ip=$(minikube ip)

echo "SmartContractAnalyzer is now running on Minikube!"
echo "Access the services using the Minikube IP: $minikube_ip"
