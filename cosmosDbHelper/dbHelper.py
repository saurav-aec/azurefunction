from cosmosDbHelper import config
from azure.cosmos import cosmos_client
from faker import Faker
from azure.cosmos.documents import DatabaseAccount
from datetime import date, timedelta
import dateutil

def connectdb():
    dbName = config.settings['database_id']
    host = config.settings['host']
    password = config.settings['master_key']
    collectionName = config.settings['container_id']

    client = cosmos_client.CosmosClient(host, {'masterKey': password}, connection_verify=False)
    return client


def deleteRecord():
    client = connectdb()
    database = client.get_database_client(config.settings["database_id"])
    container = database.get_container_client(config.settings["container_id"])

    records = getRecord()
    deleted = 0
    for r in records:
        container.delete_item(r, r['type'])
        deleted += 1
    
    print("Deleted {0} records.".format(deleted))


def getRecord():
    client = connectdb()
    database = client.get_database_client(config.settings["database_id"])
    container = database.get_container_client(config.settings["container_id"])
    
    items = list(container.read_all_items())
    print("{0} records found.".format(len(items)))
    return items


def addRecord(data):
    client = connectdb()
    database = client.get_database_client(config.settings["database_id"])
    container = database.get_container_client(config.settings["container_id"])
    
    container.upsert_item(data)
    #, response_hook = onComplete)

def onComplete(headers, data):
    print("HEADERS")
    print("-"*50)
    for k in headers:
        print(k + ": " + headers[k] )
    print("DATA")
    for k in data:
         print("{0}: {1}".format(k,data[k]))