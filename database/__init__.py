from pymongo import MongoClient
from pathlib import Path
from dotenv import load_dotenv
import os


env_file_path = Path(os.getcwd()) / ".env"
print(env_file_path)
load_dotenv(env_file_path)
mongo_url = os.getenv("MONGO_DB_URL")
learn = os.getenv("DATABASE_NAME_1")
family = os.getenv("DATABASE_NAME_2")
# fastApiOnline_learn = os.getenv("COLLECTION_NAME_1_1")
# ganesh_learn = os.getenv("COLLECTION_NAME_1_2")
# template_fam = os.getenv("COLLECTION_NAME_2_1")
client = MongoClient(mongo_url)

db1 = client[learn]
fastApiOnline_learn = db1[os.getenv("COLLECTION_NAME_1_1")]
ganesh_learn = db1[os.getenv("COLLECTION_NAME_1_2")]

db2 = client[family]
template = db2[os.getenv("COLLECTION_NAME_2_1")]

__all__ = [client, fastApiOnline_learn, ganesh_learn, template]