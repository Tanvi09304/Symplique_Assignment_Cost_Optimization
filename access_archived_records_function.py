def get_billing_record(record_id):
    item = cosmos_query_by_id(record_id)
    if item:
        return item

    blob_name = f"{record_id}.json"
    blob = blob_client.get_blob_client(container="billing-archive", blob=blob_name)
    if blob.exists():
        data = blob.download_blob().readall()
        return json.loads(data)

    return {"error": "Record not found"}
