events = {"visits": [], "conversions": []}

def log_event(event: dict):
    if event["event_type"] == "visit":
        events["visits"].append(event)
    elif event["event_type"] == "conversion":
        events["conversions"].append(event)

def get_events():
    return events
