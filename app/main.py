from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from dotenv import load_dotenv

if os.getenv("ENV") != "local":
    load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HOT_PEPPER_BASE_URL = os.getenv("HOT_PEPPER_BASE_URL")
API_KEY = os.getenv("API_KEY")  # .env から API_KEY を取得

def get_gourmet_data(large_area: str):
    params = {
        "key": API_KEY,
        "large_area": large_area,
        "format": "json"
    }
    
    response = requests.get(HOT_PEPPER_BASE_URL, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="API request failed")
    return response.json()

@app.get("/")
async def root():
    return {"message": "Hello World From Fast API"}

@app.get("/gourmet/")
async def gourmet_search(large_area: str = "Z011"):
    data = get_gourmet_data(large_area)
    return data
