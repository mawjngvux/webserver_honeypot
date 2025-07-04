from pymongo import MongoClient
from config.config import Config

# client = MongoClient(Config.MONGOURI)
client = MongoClient("mongodb://localhost:27017/")
db = client["webserverhoneypotdb"]

def get_collection(name):
    return db[name]