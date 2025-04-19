from fastapi import FastAPI
import random
app = FastAPI()

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

@app.get("/funcaoteste")
async def funcaoteste1():
    return {"teste": True, "numero aleatorio": random.randint(1, 1000)}