from pydantic import BaseModel
from datetime import datetime
from typing import Dict, List


#define thye  structure of an event eg visit or conversion
class Event(BaseModel):
    event_type: str  # type of event  "visit" or "conversion"
    timestamp: datetime
    metadata: Dict[str, str]  # Additional data (e.g., user ID, page URL)

#define the structure of a setting 
class Setting(BaseModel):
    label: str #name of the setting 
    type: str # wtype of setting  eg text 
    required: True
    default: str

#define the structurew of the payload sent by telex
class ConversionPayload(BaseModel):
    channel_id: str # id of the telex channel 
    return_url: str # url to send results back to telex 
    settings: List[Setting] # list of settings eg interval 
