from  fastapi import APIRouter,  HTTPException
from app.models import Event
from app.storage.memory import log_event



router = APIRouter ()

@router.post("/log-event")
async def log_event_endpoint(event: Event):
    if event.event_type not in ["visit", "conversion"]:
        raise HTTPException(status_code=400, detail="Invalid event type")
    
    # Log the event
    log_event(event.dict())
    return {"status": "success"}