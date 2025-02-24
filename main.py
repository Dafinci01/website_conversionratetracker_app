from fastapi import FastAPI
from app.endpoints import integration, tick, log_event

#initialize fast api app
app = FastAPI()

#include routers (endpoints) from oother files 

app.include_router(integration.router) #/integration.json endpoint
app.include_router(tick.router) #/tick endpoint 
app.include_router(log_event.router)


#Root endpoin to check ehther app is running 
@app.get("/")
def read_root():
    return{"message": "Conversion Tracker is running!"}
