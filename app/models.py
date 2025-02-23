from pydantic import BaseModel
from datetime import datetime
from typing import Dict, List

class Event(BaseModel):
    event_type: str  # "visit" or "conversion"
    timestamp: datetime
    metadata: Dict[str, str]  # Additional data (e.g., user ID, page URL)

class Setting(BaseModel):
    label: str
    type: str
    required: bool
    default: str

class ConversionPayload(BaseModel):
    channel_id: str
    return_url: str
    settings: List[Setting]
