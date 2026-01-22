from taxipred.utils.constants import COMPLETED_DATA_PATH
import pandas as pd
import json
from pydantic import BaseModel, Field, model_validator
from typing import Literal
    
class TaxiInput(BaseModel):
    Trip_Distance_km: float = Field(ge=1.0, le=60.0)
    Day_of_Week: Literal["Weekday", "Weekend"] = "Weekday"
    Passenger_Count: Literal[1, 2, 3, 4] = 3
    Traffic_Conditions: Literal["Low", "High", "Medium"] = "Medium"
    Weather: Literal["Clear", "Rain", "Snow"] = "Clear"

    Trip_Duration_Minutes: float | None = None

    # I took help from Ai with @model_validator and I took help with the calculation.
    @model_validator(mode="after")
    def calculate_trip_duration(self):
        AVG_SPEED_KMH = 60.0
        self.Trip_Duration_Minutes = (self.Trip_Distance_km / AVG_SPEED_KMH) * 60
        return self
    
class TaxiData:
    def __init__(self):
        self.df = pd.read_csv(COMPLETED_DATA_PATH)

    def to_json(self):
        return json.loads(self.df.to_json(orient="records"))

class PredictionOutput(BaseModel):   
    predicted_price: float