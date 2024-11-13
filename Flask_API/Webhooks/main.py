from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{user}")
async def greeting(user):
    return {"Hello": user}

@app.post("/webhook")
async def receive_webhook(request: Request):
    result = await request.json()
    print(result)

