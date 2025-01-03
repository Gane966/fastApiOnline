from fastapi import APIRouter, Query
from schemas.monogo_connections import CollectionStatus, DatabaseType, CollectionType
# from database.mongo import status_of_fast_api_online, status_of_ganesh_learn, status_of_template
from enum import Enum

router3 = APIRouter(tags=["database"])


# @router3.get("/fastApiOnline/status", response_model=CollectionStatus)
# async def get_connection_status():
#     connection = status_of_fast_api_online()
#     print("connection ________________________________________________________________________")
#     print(connection)
#     return {"response": '', "message": ""}
#
#
# @router3.get("/learning/status", response_model=CollectionStatus)
# async def get_connection_status():
#     connection = status_of_ganesh_learn()
#     return {"response": connection.success, "message": connection.message}
#
#
# @router3.get("/template/status", response_model=CollectionStatus)
# async def get_connection_status():
#     connection = status_of_template()
#     return {"response": connection.success, "message": connection.message}


@router3.get("/data/find")
async def find_data(
    database: DatabaseType = Query(..., description="Select the database type"),
    collection: CollectionType = Query(..., description="Select the collection type")
):
    print("111111111111111111111")
    return {"database": database, "collection": collection}

