import azure.functions as func
import datetime
from azure.cosmos import CosmosClient
from azure.storage.blob import BlobServiceClient
import json

def main(mytimer: func.TimerRequest) -> None:
    cosmos_client = CosmosClient("<COSMOS_ENDPOINT>", "<KEY>")
    db = cosmos_client.get_database_client("BillingDB")
    container = db.get_container_client("Records")

    blob_client = BlobServiceClient.from_connection_string("<BLOB_CONN_STR>")
    container_name = "billing-archive"

    threshold_date = datetime.datetime.utcnow() - datetime.timedelta(days=90)
    query = f"SELECT * FROM c WHERE c.timestamp < '{threshold_date.isoformat()}'"

    for item in container.query_items(query, enable_cross_partition_query=True):
        blob_name = f"{item['id']}.json"
        blob = blob_client.get_blob_client(container=container_name, blob=blob_name)
        blob.upload_blob(json.dumps(item), overwrite=True)

        # Optionally delete or flag record in Cosmos DB
        # container.delete_item(item['id'], partition_key=item['partitionKey'])
