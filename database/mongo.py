from . import fastApiOnline_learn, ganesh_learn, template
from models.mongo_responses import MongoResponse
from pymongo.errors import PyMongoError


# curd operations for fastApiOnline_learn
def insert_into_fast_api_online(data: list[dict], multiple: bool) -> MongoResponse:
    """
    Insert documents into 'fastApiOnline_learn'.
    If 'multiple' is True, insert many documents, otherwise insert one document.
    """
    if not data or not isinstance(data, list):
        return MongoResponse(success=False, error="Data must be a list.")

    if not all(isinstance(d, dict) for d in data):
        return MongoResponse(success=False, error="Each item in data must be a dictionary.")

    try:
        if multiple:
            result = fastApiOnline_learn.insert_many(data)
            return MongoResponse(success=True, inserted_ids=result.inserted_ids)
        else:
            result = fastApiOnline_learn.insert_one(data[0])  # data[0] for single document
            return MongoResponse(success=True, inserted_ids=[result.inserted_id])
    except PyMongoError as e:
        return MongoResponse(success=False, error=str(e))


def find_in_fast_api_online(query: dict = None) -> MongoResponse:
    """
    Find documents in 'fastApiOnline_learn' that match the query.
    """
    try:
        query = query or {}  # Default to an empty query (fetch all)
        documents = list(fastApiOnline_learn.find(query))
        return MongoResponse(success=True, documents=documents)
    except PyMongoError as e:
        return MongoResponse(success=False, error=str(e))


def update_in_fast_api_online(query: dict, update_data: dict) -> MongoResponse:
    """
    Update documents in 'fastApiOnline_learn' based on the query.
    """
    if not isinstance(query, dict) or not isinstance(update_data, dict):
        return MongoResponse(success=False, error="Query and update data must be dictionaries.")

    try:
        result = fastApiOnline_learn.update_many(query, {"$set": update_data})
        return MongoResponse(success=True, modified_count=result.modified_count)
    except PyMongoError as e:
        return MongoResponse(success=False, error=str(e))


def delete_in_fast_api_online(query: dict, multiple: bool) -> MongoResponse:
    """
    Delete documents in 'fastApiOnline_learn' based on the query.
    """
    if not isinstance(query, dict) or not isinstance(multiple, bool):
        return MongoResponse(success=False, error="query must be dict type and multiple should be bool")

    try:
        if multiple:
            result = fastApiOnline_learn.delete_many(query)
            return MongoResponse(success=True, deleted_count=result.deleted_count)
        else:
            result = fastApiOnline_learn.delete_one(query)
            return MongoResponse(success=True, deleted_count=result.deleted_count)
    except PyMongoError as e:
        return MongoResponse(success=False, error=str(e))


def status_of_fast_api_online() -> MongoResponse:
    """
    Returns the collection object 'fastApiOnline_learn'.
    """
    try:
        return MongoResponse(success=True, message="Collection fetched successfully")
    except PyMongoError as e:
        return MongoResponse(success=False, error=str(e))


# curd operations for ganesh_learn
def insert_into_ganesh_learn(data: list[dict], multiple: bool) -> MongoResponse:
    """
    Insert documents into 'fastApiOnline_learn'.
    If 'multiple' is True, insert many documents, otherwise insert one document.
    """
    if not data or not isinstance(data, list):
        return MongoResponse(success=False, error="Data must be a list.")

    if not all(isinstance(d, dict) for d in data):
        return MongoResponse(success=False, error="Each item in data must be a dictionary.")

    try:
        if multiple:
            result = ganesh_learn.insert_many(data)
            return MongoResponse(success=True, inserted_ids=result.inserted_ids)
        else:
            result = fastApiOnline_learn.insert_one(data[0])  # data[0] for single document
            return MongoResponse(success=True, inserted_ids=[result.inserted_id])
    except PyMongoError as e:
        return MongoResponse(success=False, error=str(e))


def find_in_ganesh_learn(query: dict = None) -> MongoResponse:
    """
    Find documents in 'fastApiOnline_learn' that match the query.
    """
    try:
        query = query or {}  # Default to an empty query (fetch all)
        documents = list(ganesh_learn.find(query))
        return MongoResponse(success=True, documents=documents)
    except PyMongoError as e:
        return MongoResponse(success=False, error=str(e))


def update_in_ganesh_learn(query: dict, update_data: dict) -> MongoResponse:
    """
    Update documents in 'fastApiOnline_learn' based on the query.
    """
    if not isinstance(query, dict) or not isinstance(update_data, dict):
        return MongoResponse(success=False, error="Query and update data must be dictionaries.")

    try:
        result = ganesh_learn.update_many(query, {"$set": update_data})
        return MongoResponse(success=True, modified_count=result.modified_count)
    except PyMongoError as e:
        return MongoResponse(success=False, error=str(e))


def delete_in_ganesh_learn(query: dict, multiple: bool) -> MongoResponse:
    """
    Delete documents in 'fastApiOnline_learn' based on the query.
    """
    if not isinstance(query, dict) or not isinstance(multiple, bool):
        return MongoResponse(success=False, error="query must be dict type and multiple should be bool")

    try:
        if multiple:
            result = ganesh_learn.delete_many(query)
            return MongoResponse(success=True, deleted_count=result.deleted_count)
        else:
            result = ganesh_learn.delete_one(query)
            return MongoResponse(success=True, deleted_count=result.deleted_count)
    except PyMongoError as e:
        return MongoResponse(success=False, error=str(e))


def status_of_ganesh_learn() -> MongoResponse:
    """
    Returns the collection object 'fastApiOnline_learn'.
    """
    try:
        return MongoResponse(success=True, message="Collection fetched successfully")
    except PyMongoError as e:
        return MongoResponse(success=False, error=str(e))


# curd operations for template
def insert_into_template(data: list[dict], multiple: bool) -> MongoResponse:
    """
    Insert documents into 'fastApiOnline_learn'.
    If 'multiple' is True, insert many documents, otherwise insert one document.
    """
    if not data or not isinstance(data, list):
        return MongoResponse(success=False, error="Data must be a list.")

    if not all(isinstance(d, dict) for d in data):
        return MongoResponse(success=False, error="Each item in data must be a dictionary.")

    try:
        if multiple:
            result = template.insert_many(data)
            return MongoResponse(success=True, inserted_ids=result.inserted_ids)
        else:
            result = template.insert_one(data[0])  # data[0] for single document
            return MongoResponse(success=True, inserted_ids=[result.inserted_id])
    except PyMongoError as e:
        return MongoResponse(success=False, error=str(e))


def find_in_template(query: dict = None) -> MongoResponse:
    """
    Find documents in 'fastApiOnline_learn' that match the query.
    """
    try:
        query = query or {}  # Default to an empty query (fetch all)
        documents = list(template.find(query))
        return MongoResponse(success=True, documents=documents)
    except PyMongoError as e:
        return MongoResponse(success=False, error=str(e))


def update_in_template(query: dict, update_data: dict) -> MongoResponse:
    """
    Update documents in 'fastApiOnline_learn' based on the query.
    """
    if not isinstance(query, dict) or not isinstance(update_data, dict):
        return MongoResponse(success=False, error="Query and update data must be dictionaries.")

    try:
        result = template.update_many(query, {"$set": update_data})
        return MongoResponse(success=True, modified_count=result.modified_count)
    except PyMongoError as e:
        return MongoResponse(success=False, error=str(e))


def delete_in_template(query: dict, multiple: bool) -> MongoResponse:
    """
    Delete documents in 'fastApiOnline_learn' based on the query.
    """
    if not isinstance(query, dict) or not isinstance(multiple, bool):
        return MongoResponse(success=False, error="query must be dict type and multiple should be bool")

    try:
        if multiple:
            result = template.delete_many(query)
            return MongoResponse(success=True, deleted_count=result.deleted_count)
        else:
            result = template.delete_one(query)
            return MongoResponse(success=True, deleted_count=result.deleted_count)
    except PyMongoError as e:
        return MongoResponse(success=False, error=str(e))


def status_of_template() -> MongoResponse:
    """
    Returns the collection object 'fastApiOnline_learn'.
    """
    try:
        return MongoResponse(success=True, message="Collection fetched successfully")
    except PyMongoError as e:
        return MongoResponse(success=False, error=str(e))
