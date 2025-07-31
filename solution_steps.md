# Step-by-Step Solution

## Architecture
- Cosmos DB for hot data
- Azure Blob for archived data
- Azure Function to archive old records
- Proxy layer to fetch from archive

## Archiving Process
- Daily timer Azure Function
- Query Cosmos for data older than 3 months
- Save to Blob Storage in JSON format
- Optional: delete or flag records

## Retrieval Process
- API wrapper layer (or logic in function)
- Check Cosmos DB first
- If not found, query blob
- Serve data with slight delay (~seconds)

## Deployment Tips
- Use CI/CD for Functions
- Use monitoring (App Insights + Azure Monitor)
