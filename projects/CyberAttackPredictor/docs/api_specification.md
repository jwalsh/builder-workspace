# CyberAttackPredictor API Specification

## Overview
This document outlines the RESTful API endpoints for the CyberAttackPredictor system.

## Base URL
`https://api.cyberattackpredictor.com/v1`

## Authentication
All API requests require authentication using OAuth 2.0 bearer tokens.

## Endpoints

### Data Ingestion
- `POST /data/ingest`
  - Description: Ingest new data into the system
  - Request Body: JSON object containing data source and payload
  - Response: 201 Created with ingestion job ID

### Predictions
- `GET /predictions/latest`
  - Description: Retrieve the latest prediction results
  - Query Parameters: 
    - `limit`: Number of results to return (default: 10)
  - Response: 200 OK with array of prediction objects

### Models
- `GET /models`
  - Description: List all available prediction models
  - Response: 200 OK with array of model objects

- `POST /models/{model_id}/train`
  - Description: Trigger training for a specific model
  - Response: 202 Accepted with training job ID

### Alerts
- `GET /alerts`
  - Description: Retrieve active alerts
  - Query Parameters:
    - `severity`: Filter by alert severity (low, medium, high)
  - Response: 200 OK with array of alert objects

## Error Handling
All endpoints return appropriate HTTP status codes and error messages in case of failures.

## Rate Limiting
API requests are limited to 1000 requests per hour per API key.
