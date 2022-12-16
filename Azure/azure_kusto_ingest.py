import json
import sys
from azure.kusto.data import KustoClient, KustoConnectionStringBuilder
from azure.kusto.data.data_format import DataFormat, IngestionMappingKind
from azure.kusto.ingest import (
    BlobDescriptor,
    FileDescriptor,
    IngestionProperties,
    IngestionStatus,
    KustoStreamingIngestClient,
    ManagedStreamingIngestClient,
    QueuedIngestClient,
    StreamDescriptor,
    ReportLevel
)

with open("config") as file:
    config = json.load(file)
class AzureKusto():
    def __init__(self):
        self.DATABASE=config.get("DATABASE")
        self.TABLE = config.get("TABLE")
        self.CLUSTER = config.get("CLUSTER")
        self.AUTHORITY_ID = config.get("AUTHORITY_ID")
        self.client = self.authenticate(self.CLUSTER, config.get("USERNAME"), config.get("PASSWORD"), self.AUTHORITY_ID)
        self.ingestion_properties = self.ingest_init()

    ##################################################################
    ##                              AUTH                            ##
    ##################################################################
    def authenticate(self, CLUSTER, USERNAME, PASSWORD, AUTHORITY_ID):
        kcsb = KustoConnectionStringBuilder.with_aad_user_password_authentication(CLUSTER, USERNAME, PASSWORD, AUTHORITY_ID)
        client = QueuedIngestClient(kcsb)

        return client

    ##################################################################
    ##                        INGESTION                             ##
    ##################################################################
    # Set up properties for ingestion
    def ingest_init(self):
        ingestion_props = IngestionProperties(
            database=self.DATABASE,
            table=self.TABLE,
            data_format=DataFormat.MULTIJSON,
            # in case status update for success are also required
            report_level=ReportLevel.FailuresAndSuccesses,
            # in case a mapping is required
            ingestion_mapping_reference=self.TABLE + "_mapping",
            ingestion_mapping_kind= IngestionMappingKind.JSON,
        )

        return ingestion_props

    def ingest_from_file(self, filename):
        # file_descriptor = FileDescriptor(filename, os.path.getsize(filename))  
        file_descriptor = FileDescriptor(filename) 
        result = self.client.ingest_from_file(file_descriptor, ingestion_properties=self.ingestion_properties)
        print(repr(result))

    def __str__(self):
        print(f"Database: {self.database}\nTable: {self.table}\nCluster: {self.cluster}\nAuthority ID: {self.authority_id}\nMapping")             

if __name__ == "__main__":
    connection = AzureKusto()
    # print(connection)
    connection.ingest_from_file(sys.argv[1])
    # connection.ingest_from_file("example.json")
    # check_status(connection.client)
