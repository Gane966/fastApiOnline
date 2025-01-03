import logging
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import DuplicateKeyError
from bson.objectid import ObjectId
from typing import Any, Dict, List, Optional, Union
from mongo_responses import MongoResponse

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG for detailed logs
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("MongoDBManager")


class MongoDBManager:
    def __init__(self, uri: str, database: str):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[database]
        logger.info("MongoDB connection initialized for database: %s", database)

    async def create(self, collection: str, document: Union[Dict, List[Dict]], unique_field: Optional[str] = None) -> MongoResponse:
        try:
            if isinstance(document, list):
                result = await self.db[collection].insert_many(document)
                inserted_ids = [str(id_) for id_ in result.inserted_ids]
                logger.info("Inserted documents into '%s': %s", collection, inserted_ids)
                return MongoResponse(success=True, message="Documents inserted successfully.", inserted_ids=inserted_ids)
            else:
                if unique_field and unique_field in document:
                    query = {unique_field: document[unique_field]}
                    exists = await self.db[collection].find_one(query)
                    if exists:
                        raise DuplicateKeyError(f"Document with {unique_field}='{document[unique_field]}' already exists.")
                result = await self.db[collection].insert_one(document)
                logger.info("Inserted document into '%s': %s", collection, result.inserted_id)
                return MongoResponse(success=True, message="Document inserted successfully.", inserted_ids=[str(result.inserted_id)])
        except DuplicateKeyError as e:
            return MongoResponse(success=False, message=str(e), error="Duplicate key error.")
        except Exception as e:
            logger.error("Error inserting document into '%s': %s", collection, e)
            return MongoResponse(success=False, message="Insertion failed.", error=str(e))
        finally:
            await self.close()

    async def read(self, collection: str, query: Dict = None, projection: Optional[Dict] = None, limit: int = 100, skip: int = 0) -> MongoResponse:
        try:
            cursor = self.db[collection].find(query or {}, projection or {}).skip(skip).limit(limit)
            documents = [doc async for doc in cursor]
            for doc in documents:
                doc["_id"] = str(doc["_id"])  # Convert ObjectId to string
            logger.info("Read %d documents from '%s'", len(documents), collection)
            return MongoResponse(success=True, message="Documents retrieved successfully.", documents=documents)
        except Exception as e:
            logger.error("Error reading documents from '%s': %s", collection, e)
            return MongoResponse(success=False, message="Failed to read documents.", error=str(e))
        finally:
            await self.close()

    async def update(self, collection: str, query: Dict, update_data: Dict, upsert: bool = False) -> MongoResponse:
        try:
            result = await self.db[collection].update_many(query, {"$set": update_data}, upsert=upsert)
            logger.info("Updated %d documents in '%s' with query: %s", result.modified_count, collection, query)
            return MongoResponse(success=True, message="Documents updated successfully.", matched_count=result.matched_count, modified_count=result.modified_count, upserted_id=str(result.upserted_id) if result.upserted_id else None)
        except Exception as e:
            logger.error("Error updating documents in '%s': %s", collection, e)
            return MongoResponse(success=False, message="Failed to update documents.", error=str(e))
        finally:
            await self.close()

    async def delete(self, collection: str, query: Dict) -> MongoResponse:
        try:
            result = await self.db[collection].delete_many(query)
            logger.info("Deleted %d documents from '%s' with query: %s", result.deleted_count, collection, query)
            return MongoResponse(success=True, message="Documents deleted successfully.", deleted_count=result.deleted_count)
        except Exception as e:
            logger.error("Error deleting documents from '%s': %s", collection, e)
            return MongoResponse(success=False, message="Failed to delete documents.", error=str(e))
        finally:
            await self.close()

    async def aggregate(self, collection: str, pipeline: List[Dict]) -> MongoResponse:
        try:
            cursor = self.db[collection].aggregate(pipeline)
            documents = [doc async for doc in cursor]
            logger.info("Aggregated documents from '%s' using pipeline: %s", collection, pipeline)
            return MongoResponse(success=True, message="Aggregation successful.", documents=documents)
        except Exception as e:
            logger.error("Error aggregating documents in '%s': %s", collection, e)
            return MongoResponse(success=False, message="Aggregation failed.", error=str(e))
        finally:
            await self.close()

    async def close(self):
        self.client.close()
        logger.info("MongoDB connection closed.")

# from . import fastApiOnline_learn, ganesh_learn, template
# from models.mongo_responses import MongoResponse
# from pymongo.errors import PyMongoError
#
#
# # curd operations for fastApiOnline_learn
# async def insert_into_fast_api_online(data: list[dict], multiple: bool) -> MongoResponse:
#     """
#     Insert documents into 'fastApiOnline_learn'.
#     If 'multiple' is True, insert many documents, otherwise insert one document.
#     """
#     if not data or not isinstance(data, list):
#         return MongoResponse(success=False, error="Data must be a list.")
#
#     if not all(isinstance(d, dict) for d in data):
#         return MongoResponse(success=False, error="Each item in data must be a dictionary.")
#
#     try:
#         if multiple:
#             result = await fastApiOnline_learn.insert_many(data)
#             return MongoResponse(success=True, inserted_ids=result.inserted_ids)
#         else:
#             result = await fastApiOnline_learn.insert_one(data[0])  # data[0] for single document
#             return MongoResponse(success=True, inserted_ids=[result.inserted_id])
#     except PyMongoError as e:
#         return MongoResponse(success=False, error=str(e))
#
#
# async def find_in_fast_api_online(query: dict = None) -> MongoResponse:
#     """
#     Find documents in 'fastApiOnline_learn' that match the query.
#     """
#     try:
#         query = query or {}  # Default to an empty query (fetch all)
#         documents = list(await fastApiOnline_learn.find(query))
#         return MongoResponse(success=True, documents=documents)
#     except PyMongoError as e:
#         return MongoResponse(success=False, error=str(e))
#
#
# async def update_in_fast_api_online(query: dict, update_data: dict) -> MongoResponse:
#     """
#     Update documents in 'fastApiOnline_learn' based on the query.
#     """
#     if not isinstance(query, dict) or not isinstance(update_data, dict):
#         return MongoResponse(success=False, error="Query and update data must be dictionaries.")
#
#     try:
#         result = await fastApiOnline_learn.update_many(query, {"$set": update_data})
#         return MongoResponse(success=True, modified_count=result.modified_count)
#     except PyMongoError as e:
#         return MongoResponse(success=False, error=str(e))
#
#
# async def delete_in_fast_api_online(query: dict, multiple: bool) -> MongoResponse:
#     """
#     Delete documents in 'fastApiOnline_learn' based on the query.
#     """
#     if not isinstance(query, dict) or not isinstance(multiple, bool):
#         return MongoResponse(success=False, error="query must be dict type and multiple should be bool")
#
#     try:
#         if multiple:
#             result = await fastApiOnline_learn.delete_many(query)
#             return MongoResponse(success=True, deleted_count=result.deleted_count)
#         else:
#             result = await fastApiOnline_learn.delete_one(query)
#             return MongoResponse(success=True, deleted_count=result.deleted_count)
#     except PyMongoError as e:
#         return MongoResponse(success=False, error=str(e))
#
#
# def status_of_fast_api_online() -> MongoResponse:
#     """
#     Returns the collection object 'fastApiOnline_learn'.
#     """
#     try:
#         return MongoResponse(success=True, message="Collection fetched successfully")
#     except PyMongoError as e:
#         return MongoResponse(success=False, error=str(e))
#
#
# # curd operations for ganesh_learn
# async def insert_into_ganesh_learn(data: list[dict], multiple: bool) -> MongoResponse:
#     """
#     Insert documents into 'fastApiOnline_learn'.
#     If 'multiple' is True, insert many documents, otherwise insert one document.
#     """
#     if not data or not isinstance(data, list):
#         return MongoResponse(success=False, error="Data must be a list.")
#
#     if not all(isinstance(d, dict) for d in data):
#         return MongoResponse(success=False, error="Each item in data must be a dictionary.")
#
#     try:
#         if multiple:
#             result = await ganesh_learn.insert_many(data)
#             return MongoResponse(success=True, inserted_ids=result.inserted_ids)
#         else:
#             result = await fastApiOnline_learn.insert_one(data[0])  # data[0] for single document
#             return MongoResponse(success=True, inserted_ids=[result.inserted_id])
#     except PyMongoError as e:
#         return MongoResponse(success=False, error=str(e))
#
#
# async def find_in_ganesh_learn(query: dict = None) -> MongoResponse:
#     """
#     Find documents in 'fastApiOnline_learn' that match the query.
#     """
#     try:
#         query = query or {}  # Default to an empty query (fetch all)
#         documents = list(await ganesh_learn.find(query))
#         return MongoResponse(success=True, documents=documents)
#     except PyMongoError as e:
#         return MongoResponse(success=False, error=str(e))
#
#
# async def update_in_ganesh_learn(query: dict, update_data: dict) -> MongoResponse:
#     """
#     Update documents in 'fastApiOnline_learn' based on the query.
#     """
#     if not isinstance(query, dict) or not isinstance(update_data, dict):
#         return MongoResponse(success=False, error="Query and update data must be dictionaries.")
#
#     try:
#         result = await ganesh_learn.update_many(query, {"$set": update_data})
#         return MongoResponse(success=True, modified_count=result.modified_count)
#     except PyMongoError as e:
#         return MongoResponse(success=False, error=str(e))
#
#
# async def delete_in_ganesh_learn(query: dict, multiple: bool) -> MongoResponse:
#     """
#     Delete documents in 'fastApiOnline_learn' based on the query.
#     """
#     if not isinstance(query, dict) or not isinstance(multiple, bool):
#         return MongoResponse(success=False, error="query must be dict type and multiple should be bool")
#
#     try:
#         if multiple:
#             result = await ganesh_learn.delete_many(query)
#             return MongoResponse(success=True, deleted_count=result.deleted_count)
#         else:
#             result = await ganesh_learn.delete_one(query)
#             return MongoResponse(success=True, deleted_count=result.deleted_count)
#     except PyMongoError as e:
#         return MongoResponse(success=False, error=str(e))
#
#
# async def status_of_ganesh_learn() -> MongoResponse:
#     """
#     Returns the collection object 'fastApiOnline_learn'.
#     """
#     try:
#         return MongoResponse(success=True, message="Collection fetched successfully")
#     except PyMongoError as e:
#         return MongoResponse(success=False, error=str(e))
#
#
# # curd operations for template
# async def insert_into_template(data: list[dict], multiple: bool) -> MongoResponse:
#     """
#     Insert documents into 'fastApiOnline_learn'.
#     If 'multiple' is True, insert many documents, otherwise insert one document.
#     """
#     if not data or not isinstance(data, list):
#         return MongoResponse(success=False, error="Data must be a list.")
#
#     if not all(isinstance(d, dict) for d in data):
#         return MongoResponse(success=False, error="Each item in data must be a dictionary.")
#
#     try:
#         if multiple:
#             result = await template.insert_many(data)
#             return MongoResponse(success=True, inserted_ids=result.inserted_ids)
#         else:
#             result = await template.insert_one(data[0])  # data[0] for single document
#             return MongoResponse(success=True, inserted_ids=[result.inserted_id])
#     except PyMongoError as e:
#         return MongoResponse(success=False, error=str(e))
#
#
# async def find_in_template(query: dict = None) -> MongoResponse:
#     """
#     Find documents in 'fastApiOnline_learn' that match the query.
#     """
#     try:
#         query = query or {}  # Default to an empty query (fetch all)
#         documents = list(await template.find(query))
#         return MongoResponse(success=True, documents=documents)
#     except PyMongoError as e:
#         return MongoResponse(success=False, error=str(e))
#
#
# async def update_in_template(query: dict, update_data: dict) -> MongoResponse:
#     """
#     Update documents in 'fastApiOnline_learn' based on the query.
#     """
#     if not isinstance(query, dict) or not isinstance(update_data, dict):
#         return MongoResponse(success=False, error="Query and update data must be dictionaries.")
#
#     try:
#         result = await template.update_many(query, {"$set": update_data})
#         return MongoResponse(success=True, modified_count=result.modified_count)
#     except PyMongoError as e:
#         return MongoResponse(success=False, error=str(e))
#
#
# async def delete_in_template(query: dict, multiple: bool) -> MongoResponse:
#     """
#     Delete documents in 'fastApiOnline_learn' based on the query.
#     """
#     if not isinstance(query, dict) or not isinstance(multiple, bool):
#         return MongoResponse(success=False, error="query must be dict type and multiple should be bool")
#
#     try:
#         if multiple:
#             result = await template.delete_many(query)
#             return MongoResponse(success=True, deleted_count=result.deleted_count)
#         else:
#             result = await template.delete_one(query)
#             return MongoResponse(success=True, deleted_count=result.deleted_count)
#     except PyMongoError as e:
#         return MongoResponse(success=False, error=str(e))
#
#
# async def status_of_template() -> MongoResponse:
#     """
#     Returns the collection object 'fastApiOnline_learn'.
#     """
#     try:
#         return MongoResponse(success=True, message="Collection fetched successfully")
#     except PyMongoError as e:
#         return MongoResponse(success=False, error=str(e))
