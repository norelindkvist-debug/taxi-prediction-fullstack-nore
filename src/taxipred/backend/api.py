from fastapi import FastAPI
from taxipred.backend.data_processing import TaxiData, TaxiInput, PredictionOutput
import pandas as pd
import joblib
from taxipred.utils.constants import MODEL_PATH

app = FastAPI()

taxi_data = TaxiData()

#input = TaxiInput()

@app.get("/taxi/")
async def read_taxi_data():
    return taxi_data.to_json()

@app.post("/taxi/predict", response_model= PredictionOutput)
async def predict_price(payload: TaxiInput):
    data_to_predict = pd.DataFrame(payload.model_dump(), index = [0])
    model = joblib.load(MODEL_PATH)
    prediction = model.predict(data_to_predict)
    return {"predicted_price": prediction[0]}
