from dataclasses import dataclass
from typing import List, Optional


@dataclass
class MongoResponse:
    success: bool
    message: Optional[str] = None
    inserted_ids: Optional[List[str]] = None
    modified_count: Optional[int] = None
    deleted_count: Optional[int] = None
    documents: Optional[List[dict]] = None
    error: Optional[str] = None
