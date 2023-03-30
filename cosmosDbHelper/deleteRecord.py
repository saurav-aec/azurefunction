import config
import connectdb
import getRecord as src
from faker import Faker
from azure.cosmos.documents import DatabaseAccount
from datetime import date, timedelta
import dateutil

def deleteRecord():
    client = connectdb.connectdb()
    database = client.get_database_client(config.settings["database_id"])
    container = database.get_container_client(config.settings["container_id"])

    records = src.getRecord()
    deleted = 0
    for r in records:
        container.delete_item(r, r['type'])
        deleted += 1
    
    print("Deleted {0} records.".format(deleted))



if __name__ == '__main__':
    deleteRecord()

