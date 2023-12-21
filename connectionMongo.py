from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import dotenv_values
import json


def insertMany(databaseMongo:str, collectionMongo:str, jsonList: list) -> None:
    """
    Function to insert many json files into MongoDB.

    Args:
        database (str): -
        collection (str): -
    """
    # [Setup]
    config   = dotenv_values(".env")
    user     = config["USER"]
    password = config["PASSWORD"]
    cluster  = config["CLUSTER"]

    # [Connection]
    uri = f"mongodb+srv://{user}:{password}@{cluster}.piriri-pororo"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    try:
        # client.admin.command('ping')
        # print("Pinged your deployment. You successfully connected to MongoDB!")
        db         = client[databaseMongo]
        collection = db[collectionMongo]
        
        collection.insert_many(jsonList)

    except Exception as e:
        print(e)