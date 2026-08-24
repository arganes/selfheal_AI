from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Self-Heal AI is running"}