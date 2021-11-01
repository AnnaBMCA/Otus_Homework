from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def read_ping():
    return {"message": "pong"}