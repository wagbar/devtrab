from fastapi import FastAPI
import random
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste")
async def funcaoteste1():
    return {"teste": True, "numero aleatorio": random.randint(1, 1000)}