import os
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError

class AzureStorage:

    def __init__(self, connection_string:str):
        from azure.storage.blob import BlobServiceClient
        
        try:
            # Create the BlobServiceClient object
            self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        except Exception as ex:
            print('Exception:')
            print(ex)

    def get_service_stats(self):
        print(self.blob_service_client.get_service_stats())
        
    def list_containers(self):
        containers = self.blob_service_client.list_containers(include_metadata=True)
        for container in containers:
            print(container['name'], container['metadata'])
            
    def create_blob_container(self, container_name):
        try:
            container_client = self.blob_service_client.create_container(name=container_name)
        except ResourceExistsError:
            print('A container with this name already exists')

    def delete_container(self, container_name):
        container_client = self.blob_service_client.get_container_client(container=container_name)
        container_client.delete_container()

    def list_blobs_flat(self, container_name):
        container_client = self.blob_service_client.get_container_client(container=container_name)

        blob_list = container_client.list_blobs()

        for blob in blob_list:
            print(f"Name: {blob.name}")
            
    def download_blob_to_file(self, container_name, blob_name):
        blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        with open(file=os.path.join('.', os.path.basename(blob_name)), mode="wb") as sample_blob:
            download_stream = blob_client.download_blob()
            sample_blob.write(download_stream.readall())
            
    def download_blob_to_string(self, container_name, blob_name):
        blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        # encoding param is necessary for readall() to return str, otherwise it returns bytes
        downloader = blob_client.download_blob(max_concurrency=1, encoding='UTF-8')
        blob_text = downloader.readall()
        print(f"Blob contents: {blob_text}")
        
        return blob_text
    
    def upload_blob_file(self, container_name, blob_path, local_path):
        container_client = self.blob_service_client.get_container_client(container=container_name)
        with open(file=local_path, mode="rb") as data:
            blob_client = container_client.upload_blob(name=os.path.join(blob_path, os.path.basename(local_path)), data=data, overwrite=True)

if __name__ == '__main__':
    # Authentication
    connection_string =  'DefaultEndpointsProtocol=https;AccountName=example;AccountKey=example_key;EndpointSuffix=example_endpoint'
    instance = AzureStorage(connection_string)
    
    # Get Service Status
    instance.get_service_stats()
    
    # List all containers
    instance.list_containers()
    
    # List all files in a specific container
    instance.list_blobs_flat('example-container')
    
    # Upload a file to a container
    instance.upload_blob_file(container_name='example-container', blob_path='test/', local_path='./requirements.txt')
    
    # Download blob to file
    instance.download_blob_to_file(container_name='example-container',blob_name='test/requirements.txt')
    
    # Download blob content to store in variable
    blob_data = instance.download_blob_to_string(container_name='example-container',blob_name='test/requirements.txt')
