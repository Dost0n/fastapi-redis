from fastapi import FastAPI
import router

app = FastAPI()


@app.get('/')
async def home():
    return {"message": "Hello world"}



app.include_router(router.router)