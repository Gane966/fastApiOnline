from pydantic import BaseModel

class ReturnSchemaTime(BaseModel):
    time: str

class ReturnSchemaDate(BaseModel):
    date: str