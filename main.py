from fastapi import FastAPI
from app.endpoints import integration, tick, log_event
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse  # For serving files 


#initialize fast api app
app = FastAPI()
# Add CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://staging.telextest.im", 
        "http://telextest.im",
        "https://staging.telex.im", 
        "https://telex.im"
    ],  # List of allowed origins
    allow_credentials=True,  # Allow cookies and credentials
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

#include routers (endpoints) from oother files 

app.include_router(integration.router) #/integration.json endpoint
app.include_router(tick.router) #/tick endpoint 
app.include_router(log_event.router)


#Root endpoin to check ehther app is running 
@app.get("/")
def read_root():
    return{"message": "Conversion Tracker is running!"}
# Endpoint to serve a logo file

@app.get("/logo")
def get_logo():
    # Return the logo file (replace "path/to/logo.png" with the actual path)
    return FileResponse("path/to/logo.png", media_type="image/png")
