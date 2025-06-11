# Tai du lieu tu database

import pandas as pd
from pymongo import MongoClient

def load_from_csv(path):
    return pd.read_csv(path)

def load_from_json(path):
    return pd.read_json(path, lines=True)

def load_from_mongo(uri, db_name, collection_name):
    client = MongoClient(uri)
    collection = client[db_name][collection_name]
    return pd.DataFrame(list(collection.find()))
