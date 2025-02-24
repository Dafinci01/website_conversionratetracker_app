from fastapi import APIRouter, Request
from fastapi.responses import FileResponse  # For serving files


#Create a router for the /integration,json endpoint


router = APIRouter()

#define the /integration.json endpoint 
@router.get("/integration.json")
async def get__integration_json(request: Request):
    base_url = str(request.base_url).rstrip("/")
    return {
        "data": {
            "date": {"created_at": "2025-02-20", "updated_at": "2025-02-20"},
            "descriptions": {
                "app_name": "Website Conversion Tracker",
                "app_description": "Tracks website conversion events and reports conversion rates",
                "app_logo": "https://iili.io/3H9ICmb.jpg",
                "app_url": base_url,
                "background_color": "#fff",
            },
            "is_active": True,
            "integration_type": "interval",
            "author": "David Odelana",
        
            "settings": [
                {
                    "label":"interval",
                    "type":"text",
                    "required": True,
                    "default":"0 * * * *"
                }
            ],
            "tick_url":f"{base_url}/tick"
        }
    }