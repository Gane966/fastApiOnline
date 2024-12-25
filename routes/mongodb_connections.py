from fastapi import APIRouter
from schemas.monogo_connections import CollectionStatus
from database.mongo import status_of_fast_api_online, status_of_ganesh_learn, status_of_template

router3 = APIRouter(tags=["database"])


@router3.get("/fastApiOnline/status", response_model=CollectionStatus)
async def get_connection_status():
    connection = status_of_fast_api_online()
    return {"response": connection.success, "message": connection.message}


@router3.get("/learning/status", response_model=CollectionStatus)
async def get_connection_status():
    connection = status_of_ganesh_learn()
    return {"response": connection.success, "message": connection.message}


@router3.get("/template/status", response_model=CollectionStatus)
async def get_connection_status():
    connection = status_of_template()
    return {"response": connection.success, "message": connection.message}
