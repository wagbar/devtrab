from fastapi import FastAPI
app = FastAPI()

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

@app.get("/funcaoteste")
async def funcaoteste1():
    return {"teste": "agora sim deu certo"}