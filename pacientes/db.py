import os
import ssl
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(
    os.getenv('MONGO_URI', 'mongodb://localhost:27017'),
    serverSelectionTimeoutMS=5000,
    tlsCAFile=certifi.where(),
)
db = client[os.getenv('MONGO_DB', 'vitaclin')]
pacientes_collection = db['pacientes']