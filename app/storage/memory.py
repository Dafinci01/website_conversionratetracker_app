#in memory storage for events (replace with a database)
events = {"visits": [], "conversions": []}



#log an event (visit or conversion)
def log_event(event: dict):
    if event["event_type"] == "visit":
        events["visits"].append(event) #added to visit list
    elif event["event_type"] == "conversion":
        events["conversions"].append(event)  # added to conversion list 

# Retrive all logged events 
def get_events():
    return {"visits": [], "conversions": []} 
