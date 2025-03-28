from fastapi import FastAPI, Request
from transformers import pipeline

app = FastAPI()

# Load model once on startup
classifier = pipeline("sentiment-analysis")

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    text = data.get("text")
    if not text:
        return {"error": "Missing 'text' in request body."}
    result = classifier(text)
    return {"result": result}
