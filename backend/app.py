from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# Dynamically locate model files relative to this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '..', 'model-training', 'linear_regression_model.pkl')
COLUMNS_PATH = os.path.join(BASE_DIR, '..', 'model-training', 'model_columns.pkl')

# Preload the trained model and column schema once at startup
model = joblib.load(MODEL_PATH)
model_columns = joblib.load(COLUMNS_PATH)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extract features
    rainfall = data.get("rainfall")
    temperature = data.get("temperature")
    humidity = data.get("humidity")
    soil_type = data.get("soil_type")
    crop_type = data.get("crop_type")
    acres = data.get("acres")

    # Prepare input as a DataFrame
    input_df = pd.DataFrame([{
        "rainfall": rainfall,
        "temperature": temperature,
        "humidity": humidity,
        "soil_type": soil_type,
        "crop_type": crop_type,
        "acres": acres
    }])

    # One-hot encode input and align with training columns
    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

    # Predict
    prediction = model.predict(input_encoded)[0]
    print(f"✅ Predicted water_required: {prediction}")

    return jsonify({"status_code": 200, "prediction_lr": float(round(float(prediction), 2))})

if __name__ == '__main__':
    app.run(debug=True)
