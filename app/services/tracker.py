from app.storage.memory import get_events



async def calculate_conversion_rate():
    events = get_events()
    total_visits = len(events["visits"])
    total_conversions = len(events["conversions"])
    rate = (total_conversions / total_visits) * 100 if total_visits > 0 else 0


    return rate, total_visits, total_conversions