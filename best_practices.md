# Best Practices for Data Tiering

- Partition Cosmos DB effectively (e.g., by month or customer)
- Use TTL if deletion is acceptable after archiving
- Compress large payloads before storing in Blob
- Use JSON or Parquet for blob archival
- Secure blob access with SAS tokens or private endpoints
- Monitor RU usage and blob costs regularly
