# ArogoAI

# Shipment Delay Prediction

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
   - Convert categorical variables to numerical using encoding techniques (e.g., One-Hot Encoding).
   - Normalize numerical features such as distance.
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
   - Compare performance across the models using the validation dataset.
   - Perform hyperparameter tuning for the selected model.

### 3. Deployment
1. **API Development**:
   - Built using Flask.
   - Accepts shipment details via a POST request in JSON format.
   - Returns a prediction: `Delayed` or `On Time`.
2. **API Features**:
   - Endpoint: `/predict`
   - Input: JSON object containing shipment details.
   - Output: Prediction result.

### 4. Documentation
1. Detailed steps for data preparation and model selection.
2. Instructions for running the API.

---

## Repository Structure
```
shipment-delay-prediction/
├── data/
│   ├── raw_data.csv       # Original dataset
│   ├── cleaned_data.csv   # Cleaned and preprocessed dataset
├── notebooks/
│   ├── data_preparation.ipynb # Data preparation and EDA
│   ├── model_training.ipynb   # Model training and evaluation
├── src/
│   ├── app.py             # Flask API implementation
│   ├── model.py           # Model training and inference
│   ├── utils.py           # Helper functions for data preprocessing
├── models/
│   ├── best_model.pkl     # Trained model
├── requirements.txt       # Dependencies
├── README.md              # Documentation
├── LICENSE                # License information
```

---

## Setup Instructions

### Prerequisites
- Python 3.7+
- Install dependencies:
```bash
pip install -r requirements.txt
```

### Run the API
1. Start the Flask server:
```bash
python src/app.py
```
2. Use the `/predict` endpoint to make predictions:
   - Example request:
     ```bash
     curl -X POST http://127.0.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d '{
         "Origin": "Mumbai",
         "Destination": "Delhi",
         "Shipment Date": "2024-12-20",
         "Vehicle Type": "Truck",
         "Distance": 1500,
         "Weather Conditions": "Clear",
         "Traffic Conditions": "Moderate"
     }'
     ```
   - Example response:
     ```json
     {
         "Prediction": "On Time"
     }
     ```

---

## Key Decisions
1. **Handling Missing Values**: Used mean/mode imputation for missing numerical and categorical features.
2. **Feature Encoding**: Applied One-Hot Encoding for categorical variables.
3. **Model Selection**: Random Forest was selected due to its superior performance on the validation dataset.
4. **API Framework**: Chose Flask for its simplicity and lightweight nature.

---

## Results
- **Best Model**: Random Forest
- **Evaluation Metrics**:
  - Accuracy: 92%
  - Precision: 89%
  - Recall: 88%
  - F1 Score: 88%

---

## Future Improvements
1. Incorporate real-time traffic and weather data.
2. Optimize the model further with advanced hyperparameter tuning.
3. Expand the API to handle batch predictions.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgements
Special thanks to the team and mentors for their guidance and support in this project.
