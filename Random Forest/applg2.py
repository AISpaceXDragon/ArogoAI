from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import joblib
import numpy as np
import pandas as pd

# Load the trained model
model = joblib.load("/Users/srimanthdhondy/Programs/Projects/ArogoAI_task/randomforestclassifier_dropped_actual_delivery_dates.joblib")

# Load saved encoders and column structure
label_encoders = joblib.load("/Users/srimanthdhondy/Programs/Projects/ArogoAI_task/label_encoders_randomtreeclassifier.pkl")  # Path to saved LabelEncoders

# Initialize FastAPI app
app = FastAPI()

# Define the request schema
class PredictionRequest(BaseModel):
    Origin: str
    Destination: str
    VehicleType: str
    Distance: int
    WeatherConditions: str
    TrafficConditions: str
    ShipmentDate: str
    PlannedDeliveryDate: str

# Define the response schema
class PredictionResponse(BaseModel):
    predicted_label: str
    confidence: float

@app.get("/")
def root():
    return {
        "message": (
            "API is running. Use /predict to get predictions. "
            "Provide the following values: Origin, Destination, VehicleType, "
            "Distance (in kilometers), WeatherConditions, TrafficConditions, "
            "ShipmentDate, PlannedDeliveryDate, ActualDeliveryDate."
        )
    }

# Preprocessing function
def preprocess_input(data: dict):
    try:
        # Convert date strings to datetime objects
        shipment_date = datetime.strptime(data["ShipmentDate"], "%Y-%m-%d")
        planned_delivery_date = datetime.strptime(data["PlannedDeliveryDate"], "%Y-%m-%d")
        #actual_delivery_date = datetime.strptime(data["ActualDeliveryDate"], "%Y-%m-%d")

        # Calculate delivery times
        expected_delivery_time = (planned_delivery_date - shipment_date).days
        #delay_delivery_time = (actual_delivery_date - planned_delivery_date).days

        # Initialize processed data dictionary
        processed_data = {
            "Distance (km)": data["Distance"],
            "Planned Duration": expected_delivery_time,
            #"Delay Duration": delay_delivery_time,
        }

        # Apply LabelEncoder to categorical columns
        for col, input_col in {
            "Vehicle Type": "VehicleType",
            "Weather Conditions": "WeatherConditions",
            "Traffic Conditions": "TrafficConditions",
            "Origin": "Origin",
            "Destination": "Destination"
        }.items():
            if data[input_col] not in label_encoders[col].classes_:
                raise HTTPException(status_code=400, detail=f"Invalid value '{data[input_col]}' for {col}")
            processed_data[col] = label_encoders[col].transform([data[input_col]])[0]

        # Combine processed features

        # Ensure all features are included in the correct order
        feature_order = [
            "Origin","Destination","Vehicle Type","Distance (km)","Weather Conditions","Traffic Conditions","Planned Duration",
        ]

        return pd.DataFrame([processed_data], columns=feature_order)

    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Invalid value for {str(e)}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

# Define a prediction route
@app.post("/predict", response_model=PredictionResponse)
def predict(input_data: PredictionRequest):
    # Preprocess input data
    processed_data = preprocess_input(input_data.model_dump())
    print(processed_data)

    # Make prediction
    predicted_label = "Delayed" if model.predict(processed_data)[0] == 1 else "On-time"
    confidence = np.max(model.predict_proba(processed_data))  # Probability of the predicted class

    return {"predicted_label": predicted_label, "confidence": confidence}