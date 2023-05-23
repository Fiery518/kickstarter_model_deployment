from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version

app = FastAPI()

class PredictionRequest(BaseModel):
    category: str
    total_funding: int
    country: str
    total_funding_rounds: int
    first_funding_date: str
    last_funding_date: str
    
class PredictionOut(BaseModel):
    success: int

@app.get("/")
def home():
    return {"helath_check": "OK", "model_version":model_version}

@app.post("/predict",response_model=PredictionOut)
def predict(payload: PredictionRequest):
    ans = predict_pipeline(payload.category, payload.total_funding,payload.country,payload.total_funding_rounds,
                           payload.first_funding_date,payload.last_funding_date)
    return {"success": success}