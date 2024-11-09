from fastapi import FastAPI
import requests

app = FastAPI()


@app.get('/blocking-request')
async def uuid_gen():
    url = ""
    r =  requests.get(url)
    uuid = r.json()[0]
    return uuid

