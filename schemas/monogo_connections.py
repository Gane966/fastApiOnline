from pydantic import BaseModel
from enum import Enum


class CollectionStatus(BaseModel):
    response: bool
    message: str


# Enum for Database Types
class DatabaseType(str, Enum):
    mongo1 = "learning"
    mongo2 = "familytree"


# Enum for Collection Types
class CollectionType(str, Enum):
    collection1 = "fastapionline"
    collection2 = "ganesh"
    collection3 = "template"
