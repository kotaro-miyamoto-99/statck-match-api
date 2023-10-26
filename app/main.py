from fastapi import FastAPI, Depends, HTTPException
import requests

app = FastAPI()

BASE_URL = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
API_KEY = "8a6819bc6cccd830"

def get_gourmet_data(large_area: str):
    params = {
        "key": API_KEY,
        "large_area": large_area,
        "format": "json"
    }
    response = requests.get(BASE_URL, params=params)
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
