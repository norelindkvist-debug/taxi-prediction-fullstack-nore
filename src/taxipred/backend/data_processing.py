from taxipred.utils.constants import DATA_PATH
import pandas as pd
import json

class TaxiData:
    def __init__(self):
        self.df = pd.read_csv(DATA_PATH/"Taxi_price_model.joblib")

    def to_json(self):
        return json.loads(self.df.to_json(orient="records"))