import logging
import azure.functions as func
import config
from cosmosDbHelper import dbHelper
from datetime import date, timedelta
import dateutil
from faker import Faker


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    fake = Faker()
    Faker.seed(100)
    dob = fake.date_between(date(1905,1,1),
          date.today()-timedelta(days=3650))
    data = { "id": "1", "type": "record", "source": "azFunc",
         "name": fake.name(),
         "age": int((date.today()-dob).days/365), 
         "dob": dob.strftime("%m-%d-%y")}
    dbHelper.addRecord(data)
    records = dbHelper.getRecord()
    if records:
        return func.HttpResponse(
             "{0} records found in db".format(len(records)),
             status_code=200
        )
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )


    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )
