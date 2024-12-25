from pydantic import BaseModel


class CollectionStatus(BaseModel):
    response: bool
    message: str
