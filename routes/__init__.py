from pathlib import Path
from dotenv import load_dotenv
from mongo import MongoDBManager
import os


env_file_path = Path(os.getcwd()) / ".env"
load_dotenv(env_file_path)
mongo_url = os.getenv("MONGO_DB_URL")
database_learn = os.getenv("DATABASE_NAME_1")
database_family = os.getenv("DATABASE_NAME_2")
COLLECTION_NAME_1_1 = os.getenv("COLLECTION_NAME_1_1")
COLLECTION_NAME_1_2 = os.getenv("COLLECTION_NAME_1_2")
COLLECTION_NAME_2_1 = os.getenv("COLLECTION_NAME_2_1")

# databases
fast_api_online = MongoDBManager(uri=mongo_url, database=database_learn)
ganesh = MongoDBManager(uri=mongo_url, database=database_learn)
template = MongoDBManager(uri=mongo_url, database=database_family)



__all__ = [mongo_url, database_learn, database_family, COLLECTION_NAME_1_1, COLLECTION_NAME_1_2, COLLECTION_NAME_2_1]