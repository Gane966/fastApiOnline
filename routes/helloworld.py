from fastapi import APIRouter
import datetime
from schemas.helloworld import ReturnSchemaTime, ReturnSchemaDate

router = APIRouter(tags=["hello"])

@router.get('/')
async def read_root():
    return {'message': f'Hello there to look into the docs please navigate to {"/docs"}'}

@router.get('/day',response_model=ReturnSchemaDate)
async def read_root():
    return {'date': f"Today's date is {datetime.datetime.now().day} -- {datetime.datetime.now().month} --"
                    f" {datetime.datetime.now().year}"}

@router.get('/time', response_model=ReturnSchemaTime)
async def read_root():
    return {'time': f"now time is {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:"
                    f"{datetime.datetime.now().second}:{datetime.datetime.now().microsecond}"}

