from fastapi import FastAPI

app = FastAPI()


@app.get("/roll")
async def root():
    
    return {"message": "dice roll is 4"}