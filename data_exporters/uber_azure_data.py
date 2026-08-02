import  pandas as pd
from io import StringIO
from azure.storage.blob import BlobServiceClient

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(df, *args, **kwargs):
    """
    Export dataframe as CSV to Azure Blob Storage
    """

    account_name = "uberstoragepranjal123"
    account_key = "YOUR_AZURE_STORAGE_KEY"

    connection_string = (
        f"DefaultEndpointsProtocol=https;"
        f"AccountName={account_name};"
        f"AccountKey={account_key};"
        f"EndpointSuffix=core.windows.net"
    )

    container_name = "uber-data"
    blob_name = "uber/uber_data.csv"

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )

    blob_client.upload_blob(csv_buffer.getvalue(), overwrite=True)

    print("CSV uploaded successfully!")

    return df
