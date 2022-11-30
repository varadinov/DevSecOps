from fastapi import FastAPI
from datetime import datetime
import socket

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World", "time": datetime.now(), "hostname": socket.gethostname()}