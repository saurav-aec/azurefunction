from cosmosDbHelper import config, connectdb
import connectdb
from faker import Faker
from azure.cosmos.documents import DatabaseAccount
from datetime import date, timedelta
import dateutil

def addRecord(data):
    client = connectdb.connectdb()
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


if __name__ == '__main__':
    fake = Faker()
    Faker.seed(100)
    count = input("Enter number of records to add: ")
    for i in range(1, int(count) + 1):
        dob = fake.date_between(date(1905,1,1),
          date.today()-timedelta(days=3650))
        addRecord({ "id": str(i), "type": "record", "source": "azFunc",
         "name": fake.name(),
         "age": int((date.today()-dob).days/365), 
         "dob": dob.strftime("%m-%d-%y")})

