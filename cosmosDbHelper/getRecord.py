from cosmosDbHelper import connectdb, config
from faker import Faker
from azure.cosmos.documents import DatabaseAccount
from datetime import date, timedelta
import dateutil

def getRecord():
    client = connectdb.connectdb()
    database = client.get_database_client(config.settings["database_id"])
    container = database.get_container_client(config.settings["container_id"])
    
    items = list(container.read_all_items())
    print("{0} records found.".format(len(items)))
    return items


if __name__ == '__main__':
    getRecord()

