from fastapi import APIRouter, Request
from fastapi.responses import FileResponse 



{
  "data": {
    "descriptions": {
      "app_name": "Website Conversion Tracker",
      "app_description": "Monitors user interactions and conversions on websites, providing real-time analytics and insights.",
      "app_url": "https://website-conversionratetracker-app.onrender.com",
      "app_logo": "https://website-conversionratetracker-app.onrender.com"/static/logo.png",
      "background_color": "#f5f5f5"
    },
    "integration_type": "interval",
    "integration_category": "Data Analytics & Visualization",
    "key_features": [
      "Tracks user actions like clicks, form submissions, and purchases",
      "Provides real-time conversion analytics",
      "Integrates with CRM and marketing tools",
      "Supports custom conversion events",
      "Generates reports and insights"
    ],
    "settings": [
      {
        "label": "Website URL",
        "type": "text",
        "required": True,
        "default": "https://example.com"
      },
      {
        "label": "Tracking ID",
        "type": "text",
        "required": True,
        "default": "CONV-123456"
      },
      {
        "label": "Conversion Event",
        "type": "text",
        "required": True,
        "default": "purchase"
      },
      {
        "label": "Notification Email",
        "type": "email",
        "required": False,
        "default": "admin@example.com"
      },
      {
        "label": "Interval",
        "type": "text",
        "required": True,
        "default": "*/5 * * * *"
      }
    ],
   "tick_url": "https://website-conversionratetracker-app.onrender.com/tick",
   "target_url": "https://website-conversionratetracker-app.onrender.com/track"
  }
}
