from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["login_system"]
user_collection = db["users"]
