# Symplique_Assignment_Cost_Optimization
Cost optimization strategy for read-heavy serverless application using Azure Cosmos DB and archival solutions.
# Azure Cosmos DB Cost Optimization for Serverless Application

This project outlines a strategy to reduce Azure Cosmos DB costs for a read-heavy serverless application.

## Problem Summary
- Large Cosmos DB with infrequent access to older records
- Need to retain historical data with reduced cost
- No API changes or downtime

## Solution Summary
- Archive records > 3 months to Azure Blob Storage
- Retrieve archived records via a proxy layer
- Use Azure Functions for archiving and retrieval

## Folders
- `architecture/`: Architecture diagram
- `scripts/`: Azure Function pseudocode/scripts
- `docs/`: Full write-up of solution and best practices
- `cache-proxy/`: Optional caching layer to maintain API contract

