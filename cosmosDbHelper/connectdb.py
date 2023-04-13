from cosmosDbHelper import config
from azure.cosmos import cosmos_client, exceptions, PartitionKey

def connectdb():
    dbName = config.settings['database_id']
    host = config.settings['host']
    password = config.settings['master_key']
    collectionName = config.settings['container_id']

    print(host)
    print(password)

    client = cosmos_client.CosmosClient(host, {'masterKey': password}, connection_verify=False)
    database = client.create_database_if_not_exists(id=dbName)
    print(database)
    database.create_container_if_not_exists(id = collectionName, partition_key = PartitionKey(path="/type"))


    return client


if __name__ == '__main__':
    client = connectdb()
    db = client.list_databases()