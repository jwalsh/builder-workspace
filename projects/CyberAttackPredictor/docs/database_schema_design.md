# CyberAttackPredictor Database Schema Design

## Overview
This document outlines the database schema for the CyberAttackPredictor system, including both relational (PostgreSQL) and NoSQL (MongoDB) databases.

## PostgreSQL Schema

### Users Table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE
);
```

### PredictionModels Table
```sql
CREATE TABLE prediction_models (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    version VARCHAR(20) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_trained TIMESTAMP WITH TIME ZONE,
    accuracy FLOAT
);
```

### Predictions Table
```sql
CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    model_id INTEGER REFERENCES prediction_models(id),
    prediction_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    prediction_result JSONB,
    confidence_score FLOAT
);
```

## MongoDB Schema

### RawData Collection
```json
{
  "_id": ObjectId,
  "source": String,
  "data_type": String,
  "timestamp": Date,
  "payload": Object
}
```

### ProcessedData Collection
```json
{
  "_id": ObjectId,
  "raw_data_id": ObjectId,
  "features": Object,
  "processed_at": Date
}
```

### Alerts Collection
```json
{
  "_id": ObjectId,
  "severity": String,
  "message": String,
  "created_at": Date,
  "resolved_at": Date,
  "related_prediction_id": ObjectId
}
```

## Indexing Strategy
- PostgreSQL: Create indexes on frequently queried columns (e.g., user email, prediction_time)
- MongoDB: Create indexes on timestamp fields and frequently queried attributes within the payload

## Data Retention Policy
- Raw data: 6 months
- Processed data: 1 year
- Predictions and alerts: 2 years
