from motor.motor_asyncio import AsyncIOMotorClient
from pathlib import Path
from dotenv import load_dotenv
import os


env_file_path = Path(os.getcwd()) / ".env"
load_dotenv(env_file_path)
mongo_url = os.getenv("MONGO_DB_URL")
database_learn = os.getenv("DATABASE_NAME_1")
database_family = os.getenv("DATABASE_NAME_2")
COLLECTION_NAME_1_1 = os.getenv("COLLECTION_NAME_1_1")
COLLECTION_NAME_1_2 = os.getenv("COLLECTION_NAME_1_2")
COLLECTION_NAME_2_1 = os.getenv("COLLECTION_NAME_2_1")

database_collection = {
    database_learn.lower(): [os.getenv("COLLECTION_NAME_1_1").lower(), os.getenv("COLLECTION_NAME_1_2").lower()],
    database_family.lower(): [os.getenv("COLLECTION_NAME_2_1").lower()]
}


__all__ = [mongo_url, database_learn, database_family, COLLECTION_NAME_1_1, COLLECTION_NAME_1_2, COLLECTION_NAME_2_1]