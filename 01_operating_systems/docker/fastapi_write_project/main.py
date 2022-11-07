from fastapi import FastAPI, HTTPException
from datetime import datetime
from os import listdir
import os
from os.path import isfile, join

app = FastAPI()

DATA_DIR = os.environ.get("FASTAPI_DATA_DIR", "/data")
  
@app.get("/")
async def root():
    return {
            "files": [f for f in listdir(DATA_DIR) if isfile(join(DATA_DIR, f))]
        }

@app.get("/get-file/{name}")
def get_file(name: str):
    if not os.path.exists(f"{DATA_DIR}/{name}"):
        raise HTTPException(404, "File not found")
    
    with open(f"{DATA_DIR}/{name}", 'r') as file:
        return file.read()

@app.get("/update-file/{name}/{data}")
def create_or_update_file(name: str, data: str):
    with open(f"{DATA_DIR}/{name}", 'w') as file:
        file.write(data)

    return {"status": "ok"}


