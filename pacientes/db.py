import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(
    os.getenv('MONGO_URI', 'mongodb://localhost:27017'),
    serverSelectionTimeoutMS=5000,
    connectTimeoutMS=5000,
    socketTimeoutMS=5000,
    tlsInsecure=True,
)
db = client[os.getenv('MONGO_DB', 'vitaclin')]
pacientes_collection = db['pacientes']