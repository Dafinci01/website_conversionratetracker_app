from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse  # Using JSONResponse to return JSON properly

router = APIRouter()

@router.get("/integration.json")
async def get_integration_json(request: Request):
    base_url = str(request.base_url).rstrip("/")  # Fixed incorrect return statement

    return JSONResponse(content={  # Using JSONResponse to ensure proper JSON format
        "data": {
            "date": {
                "created_at": "2025-02-20",
                "updated_at": "2025-02-24"
            },
            "descriptions": {
                "app_name": "website-conversionratetracker-app",
                "app_description": "Data Analytics & Visualization",
                "app_logo": "https://website-conversionratetracker-app.onrender.com/static/data_analytics.png",
                "app_url": "https://website-conversionratetracker-app.onrender.com/",
                "background_color": "#fff"
            },
            "is_active": True,
            "integration_type": "interval",
            "integration_category": "Data Analytics & Visualization",
            "key_features": [
                "Tracks user actions like clicks",
                "form submissions",
                "and purchases",
                "Detailed analytics on visitor behavior",
                "Multi-device tracking"
            ],
            "author": "Davidodelana",
            "settings": [
                {
                    "label": "1hr",
                    "type": "text",
                    "required": True,
                    "default": "website_conversionratetracker_app"
                }
            ],
            "target_url": "https://website-conversionratetracker-app.onrender.com/integration.json/target",
            "tick_url": "https://website-conversionratetracker-app.onrender.com/integration.json/tick"
        }
    })
