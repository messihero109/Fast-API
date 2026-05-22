from fastapi import FastAPI
import pandas as pd
from app.schema import cardio
from app.model import load_model_scaler

model, scaler = load_model_scaler()

app = FastAPI()

# post (insert/Create/Send), get (Update), get(Read/Select/Retrieve), delete(Remove)

# home page
@app.get("/")
def home():
    return 'Welcome to Cardiovascular Disease Prediction Fast API Application '

# @app.get("/cardio-predict")
# def home():
#      return 'Cardiovascular Disease Prediction Application'

@app.post("/Predict-cardio")
def predict(data:cardio):
    input_data = pd.DataFrame([
         data.model_dump()  # convert sent data from application and convert it to JSON format.
    ])
    input_scaler = scaler.transform(input_data)
    prediction = model.predict(input_scaler) [0]
    return{
        "Prediction_Status": int(prediction),
        "Status": "Likely to be Healthy" if prediction == 0 else "Likely to be Unhealthy"
    }


