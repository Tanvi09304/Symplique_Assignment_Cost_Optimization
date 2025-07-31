# Transparent Cache/Proxy Layer

## Goal
Serve data from Cosmos DB if available, fallback to archive without changing API clients.

## Logic (Pseudocode)
```python
def get_record(record_id):
    if cache.exists(record_id):
        return cache.get(record_id)

    record = cosmos_db.get(record_id)
    if record:
        cache.set(record_id, record)
        return record

    archive = blob_storage.get(record_id)
    if archive:
        cache.set(record_id, archive)
        return archive

    return None
```

## Technologies
- Azure Redis Cache
- Azure API Management
- Azure Front Door (optional)
