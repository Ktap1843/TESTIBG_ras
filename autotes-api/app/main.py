from fastapi import FastAPI

app = FastAPI(title="Autotest REST API")

@app.get("/")
async def root():
    return {"message": "API is working!"}
