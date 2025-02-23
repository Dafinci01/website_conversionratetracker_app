from fastapi import APIRouter, Request



#Create a router for the /integration,json endpoint


router = APIRouter

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
            "key_features": ["- Data Analytics"],
            "integration_category": "Data Analytics & Visualization",
            "author": "David Odelana",
        
            "settings": [
                {"label": "site-1", "type": "text", "required": True, "default": ""},
                {"label": "site-2", "type": "text", "required": True, "default": ""},
                {"label": "target_url", "type": "text", "required": True, "default": ""},
                {"label": "interval", "type": "text", "required": True, "default": "* * * * *"}
            ],
            "tick_url":"https://ping.telex.im/v1/webhooks/0195326e-b2df-79b7-99bb-c07e4aabd362"
        }
    }