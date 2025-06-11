from pymongo import MongoClient
from config.config import Config

client = MongoClient(Config.MONGOURI)
db = client[Config.MONGO_DB_NAME]

def get_collection(name):
    return db[name]