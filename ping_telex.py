import httpx
from fastapi import APIRouter

router = APIRouter()

TELEX_WEBHOOK_URL = "https://ping.telex.im/v1/webhooks/01951ca7-a0cf-78b8-8218-4df86c56da46"

@router.get("/ping-telex")
async def ping_telex():
    """Sends a properly formatted request to Telex API"""
    payload = {
        "event_name": "curl POST",
        "message": "a first ping",
        "username": "David testing",
        "status": "active"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(TELEX_WEBHOOK_URL, json=payload)

    if response.status_code == 200:
        return {"status": "success", "response": response.json()}
    else:
        return {"status": "failed", "error": response.text}
