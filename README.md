# MobilityLakehouse

## Overview
MobilityLakehouse is a data engineering project built using Databricks, PySpark, and Delta Lake. It processes mobility-related datasets such as customers, drivers, trips, payments, locations, and vehicles using a multi-layer architecture.

## Architecture
Source: CSV files stored in Databricks Volumes  
Processing: PySpark Structured Streaming  
Storage: Delta Lake (Lakehouse architecture)

## Medallion Architecture:
- Bronze Layer → Raw streaming ingestion
- Silver Layer → Cleaned and transformed data
- Gold Layer → Business aggregations and analytics

## Additional Features:
- Streaming checkpoints implemented for fault tolerance and recovery
- Unity Catalog used for organizing schemas and Delta tables

## Datasets Used
Customers  
Drivers  
Trips  
Payments  
Locations  
Vehicles  

## Technologies Used

- Databricks
- PySpark
- Delta Lake
- Structured Streaming
- SQL 

## Current Progress

### Bronze Layer
- Streaming ingestion completed
- Delta bronze tables created
- Structured Streaming checkpoints implemented

### Silver Layer
- Customer transformations implemented
- Email domain extraction
- Full name generation
- Deduplication using Window functions
- Process timestamp tracking
- Delta write operations in progress
- Reusable Delta Lake upsert/merge utility implemented
- CDC-based merge condition handling added

### Gold Layer
- Planned 

## Future Work

- Build Gold layer business aggregations
- Add data quality validation checks
- Optimize ingestion using Auto Loader
- Implement orchestration workflows
- Add dashboard/reporting layer
  Data quality checks  
  Optimization using Auto Loader

## Project status
  In Progress
