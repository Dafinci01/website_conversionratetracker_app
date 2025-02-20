import asyncio
import json
from fastapi import FastAPI, BackgroundTasks, Request
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import httpx

# Define payload model
class Setting(BaseModel):
    label: str
    type: str
    required: bool
    default: str

class tickPayload(BaseModel):
    channel_id: str
    return_url: str
    settings: List[Setting]

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://staging.telextest.im", "http://telextest.im",
        "https://staging.telex.im", "https://telex.im"
    ],  # NB: telextest is a local URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/logo")
def get_logo():
    return FileResponse("uptime.png")

# Integration JSON endpoint
@app.get("/integration.json")
def get_integration_json(request: Request):
    base_url = str(request.base_url).rstrip("/")
    
    return {
        "data": {
            "date": {"created_at": "2025-02-20", "updated_at": "2025-02-20"},
            "descriptions": {
                "app_name": "Website Conversion Tracker",
                "app_description": "Tracks website conversion events and reports conversion rates",
                "app_logo": "https://i.imgur.com/lZqvffp.png",
                "app_url": base_url,
                "background_color": "#fff",
            },
            "is_active": False,
            "integration_type": "interval",
            "key_features": ["- Data Analytics"],
            "integration_category": "Data Analytics & Visualization",
            "author": "David Odelana",
            "website": base_url,
            "settings": [
                {"label": "site-1", "type": "text", "required": True, "default": ""},
                {"label": "site-2", "type": "text", "required": True, "default": ""},
                {"label": "interval", "type": "text", "required": True, "default": "* * * * *"},
                {"label": "tracking_url", "type": "text", "required": True, "default": ""}
            ],
            "tracking_url": "",
            "tick_url": f"{base_url}/tick"
        }
    }

# Function to process conversion data
async def get_conversion_data(tracking_url: str) -> str:
    """Fetch conversion data from the given tracking_url"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(tracking_url, timeout=10)
            if response.status_code < 400:
                return response.text  # Conversion data report
            return f"Error fetching data: {response.status_code}"
    except Exception as e:
        return f"Exception: {str(e)}"

# Processing the tick
async def process_tick(payload: tickPayload):
    """Extract tracking_url, fetch conversion data, and send the report"""
    
    # Use next() to fetch tracking_url directly instead of looping
    tracking_url = next((s.default for s in payload.settings if s.label == "tracking_url"), "")

    report = await get_conversion_data(tracking_url)

    # Format response to Telex
    data = {
        "message": report,
        "username": "Conversion Tracker",
        "event_name": "Conversion Report",
        "status": "success"
    }

    # Send the report to the return_url provided by Telex
    async with httpx.AsyncClient() as client:
        await client.post(payload.return_url, json=data)

# Tick endpoint
@app.post("/tick", status_code=202)
def tick_endpoint(payload: tickPayload, background_tasks: BackgroundTasks):
    """Immediately returns 202 and runs monitoring in the background."""
    background_tasks.add_task(process_tick, payload)
    return {"status": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

