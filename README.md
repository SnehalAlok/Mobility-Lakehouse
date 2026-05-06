# MobilityLakehouse

## Overview
MobilityLakehouse is a data engineering project built using Databricks, PySpark, and Delta Lake. It processes mobility-related datasets such as customers, drivers, trips, payments, locations, and vehicles using a multi-layer architecture.

## Architecture
Source: CSV files stored in Databricks Volumes  
Processing: PySpark Structured Streaming  
Storage: Delta Lake (Lakehouse architecture)

## Datasets Used
Customers  
Drivers  
Trips  
Payments  
Locations  
Vehicles  

## Technologies Used
Databricks  
PySpark  
Delta Lake  
Structured Streaming  

## Current Progress
Bronze Layer: Streaming ingestion completed  
Silver Layer: In progress  
Gold Layer: Planned  

## Future Work
Data cleaning and transformations in Silver layer  
Business aggregations in Gold layer  
Data quality checks  
Optimization using Auto Loader
