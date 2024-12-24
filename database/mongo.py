from pymongo import MongoClient
from pathlib import Path
from dotenv import load_dotenv
import os


env_file_path = Path(os.getcwd()).parent / ".env"
load_dotenv(env_file_path)
mongo_url = os.getenv("MONGO_DB_URL")
client = MongoClient(mongo_url)
