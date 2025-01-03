from mongo import *
from . import database_collection
from typing import Callable, Dict, Any
from mongo import (
    find_in_fast_api_online,
    insert_into_fast_api_online,
    update_in_fast_api_online,
    delete_in_fast_api_online,
    find_in_ganesh_learn,
    insert_into_ganesh_learn,
    update_in_ganesh_learn,
    delete_in_ganesh_learn,
    find_in_template,
    insert_into_template,
    update_in_template,
    delete_in_template)

collection_operations = {
    "fast_api_online": {
        "find": find_in_fast_api_online,
        "insert": insert_into_fast_api_online,
        "update": update_in_fast_api_online,
        "delete": delete_in_fast_api_online,
    },
    "ganesh": {
        "find": find_in_ganesh_learn,
        "insert": insert_into_ganesh_learn,
        "update": update_in_ganesh_learn,
        "delete": delete_in_ganesh_learn,
    },
    "template": {
        "find": find_in_template,
        "insert": insert_into_template,
        "update": update_in_template,
        "delete": delete_in_template,
    },
}


async def fetching_values(database, collection, user_query: dict, insert_data: dict, update_val: dict,
                          api_type: str):
    if collection.lower() in database_collection[database.lower()]:
        print("")

    return True
