from fastapi import APIRouter, BackgroundTasks
from app.models import ConversionPayload
from app.services.tracker import calculate_conversion_rate
import httpx

router = APIRouter()

@router.post("/tick", status_code=200)
async def tick(payload: ConversionPayload, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_report, payload.return_url)
    return {"status": "accepted"}

async def send_report(target_url: str):
    # ✅ Use `await` to call the async function
    rate, visits, conversions =  calculate_conversion_rate()
    message = f"Conversion Rate: {rate:.2f}% ({conversions}/{visits})"

    # Format for telex
    data = {
        "message": message,
        "username": "Conversion Tracker",
        "event_name": "Hourly Report",
        "status": "info"
    }
    async with httpx.AsyncClient() as client:
        await client.post(return_url, json=data)