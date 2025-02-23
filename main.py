from fastapi import FastAPI
from app.endpoints import integration, tick, log_event






app = FastAPI()
#include routers 

app.include_router(integration.router)
app.include_router(tick.router)
app.include_router(log_event.router)



@app.get("/")
def read_root():
    return("message": "Conversion Tracker is running!")
