# ArogoAI

# Task 1: Shipment Delay Prediction

## Objective
This repository contains the solution to the Shipment Delay Prediction problem, which aims to predict whether a shipment will be delayed or on time based on historical data. The project involves data preparation, model development, and deployment of an API for predictions.

---

## Dataset Details
The dataset includes the following features:
- **Shipment ID**: Unique identifier for each shipment.
- **Origin**: Origin city of the shipment (Indian cities).
- **Destination**: Destination city of the shipment (Indian cities).
- **Shipment Date**: Date of shipment.
- **Planned Delivery Date**: The expected date for the product to be delivered.
- **Actual Delivery Date**: The Actual Date of Delivery of the product.
- **Vehicle Type**: Type of vehicle (Truck, Lorry, Container, Trailer).
- **Distance**: Distance in kilometers.
- **Weather Conditions**: Weather during shipment (Clear, Rain, Fog).
- **Traffic Conditions**: Traffic level during shipment (Light, Moderate, Heavy).
- **Delay**: Target variable indicating whether the shipment was delayed (Yes/No).

---

## Solution Workflow
### 1. Data Preparation & Exploration
1. **Data Cleaning**: Handle missing values by removing them.I have removed the null values(597 null values from "Vehicle Type" out of which 438 values were having "Delayed" as "Yes" and the remaining were "No") instead of imputing them with various values.
2. **Feature Engineering**:
   - Convert categorical variables to numerical using encoding techniques (e.g., Label Encoding).
   - I have purposefully dropped the "Actual Delivery Date", otherwise it would not be requiring ML algorithms for the prediction.It would only require an if-else statement to decide if the delivery is "Delayed" or "On-time".The other reason why I have done this step is to simulate real world scenarios.It is because in real life we would be making a prediction before the delivery is being done and not after the actual delivery.
3. **Exploratory Data Analysis (EDA)**:
   - Visualize relationships between features and the target variable.
   - Identify feature importance using correlation analysis or feature importance metrics.

### 2. Model Development
1. **Algorithms**:
   - Logistic Regression
   - Random Forest
2. **Evaluation Metrics**:
   - Accuracy
   - Precision
   - Recall
   - F1 Score
3. **Model Selection**:
   - Compare performance across the models using the test dataset.
   - Perform hyperparameter tuning for the selected model using Grid Search from the sklearn library.

### 3. Deployment
1. **API Development**:
   - Built using Fastapi.
   - Accepts shipment details via a POST request in JSON format.
   - Returns a prediction: `Delayed` or `On Time`.
2. **API Features**:
   - Endpoint: `/predict`
   - Input: JSON object containing shipment details.
   - Output: Prediction result.

### 4. Documentation
1. Detailed steps for data preparation and model selection:
   - **Data Preparation**:
     - Addressed missing values by dropping them.
     - Encoded categorical variables and introduced new column "Planned Duration".
   - **Model Selection**:
     - Conducted comparisons of Logistic Regression and Random Forest models.
     - Evaluated metrics (Accuracy, Precision, Recall, F1 Score).
     - Used cross-validation to validate model robustness and prevent overfitting.

2. Instructions for running the API:
   - Download or clone this repository and you will have the weights of the trained models along with the label encoders used while training.
   - Input these file paths into the python file "applg2.py" and run the program.
   - Run the following command from terminal/command prompt:
     ```bash
     uvicorn applg2:app --reload
     ```
   - Then go the website "http://127.0.0.1:8000/docs" and give the input to the API. (OR)
   - Use the `/predict` endpoint to make predictions:
   - Example request:
     ```bash
     curl -X 'POST' \
     'http://127.0.0.1:8000/predict' \
     -H 'accept: application/json' \
     -H 'Content-Type: application/json' \
     -d '{
     "Origin": "Pune",
     "Destination": "Jaipur",
     "VehicleType": "Truck",
     "Distance": 1172,
     "WeatherConditions": "Storm",
     "TrafficConditions": "Light",
     "ShipmentDate": "2023-09-08",
     "PlannedDeliveryDate": "2023-09-10"
      }'
     ```
   - Example response:
     ```json
     {
         "predicted_label": "On Time",
         "confidence": 0.88231987
     }
     ```

---

## Key Decisions
1. **Handling Missing Values**: Dropped the missing numerical and categorical features.
2. **Feature Encoding**: Applied Label Encoding for categorical variables.
3. **Model Selection**: Random Forest was selected due to its superior performance on the test dataset.
4. **API Framework**: Chose Fastapi for its simplicity and lightweight nature.

---

## Results
- **Best Model**: Random Forest
- **Evaluation Metrics for Random Forest**:
  - Accuracy: 94%
  - Precision: 98%
  - Recall: 90%
  - F1 Score: 94%
- **Evaluation Metrics for Logistic Regression**:
  - Accuracy: 88%
  - Precision: 100%
  - Recall: 75%
  - F1 Score: 85%
---

## Future Improvements
1. Incorporate real-time traffic and weather data.
2. Optimize the model further with advanced hyperparameter tuning.
3. Expand the API to handle batch predictions.
