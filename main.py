from fastapi import FastAPI, HTTPException  # Correct casing
from ping_telex import router as ping_router


app = FastAPI()

# Include the ping router
app.include_router(ping_router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

