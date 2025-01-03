from dataclasses import dataclass
from typing import List, Optional, Dict, Any


@dataclass
@dataclass
class MongoResponse:
    success: bool
    message: Optional[str] = None
    inserted_ids: Optional[List[str]] = None
    matched_count: Optional[int] = None
    modified_count: Optional[int] = None
    deleted_count: Optional[int] = None
    documents: Optional[List[Dict]] = None
    upserted_id: Optional[str] = None
    acknowledged: Optional[bool] = None
    error: Optional[str] = None
    raw_result: Optional[Any] = None

