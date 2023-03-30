from cosmosDbHelper import config
from azure.cosmos import cosmos_client

def connectdb():
    dbName = config.settings['database_id']
    host = config.settings['host']
    password = config.settings['master_key']
    collectionName = config.settings['container_id']

    client = cosmos_client.CosmosClient(host, {'masterKey': password}, connection_verify=False)
    return client


if __name__ == '__main__':
    client = connectdb()
    db = client.list_databases()
    for d in db:
        print(d)