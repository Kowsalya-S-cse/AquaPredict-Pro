# 💧 AquaPredict Pro — AI-Based Crop Water Prediction System

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://aquapredict-pro.streamlit.app)
[![Flask](https://img.shields.io/badge/Flask-3.0+-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.4+-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github&logoColor=white)](https://github.com/Kowsalya-S-cse/AquaPredict-Pro)

**AquaPredict Pro** is an intelligent precision agriculture system designed to eliminate guesswork in agricultural irrigation. By analyzing key soil, crop, and atmospheric conditions (temperature, humidity, rainfall, soil type, and acreage), it delivers instant, data-driven irrigation predictions and localized conservation recommendations to prevent overwatering and maximize crop yields.

> 🌐 **Live Web Application:** [https://aquapredict-pro.streamlit.app](https://aquapredict-pro.streamlit.app)  
> 💻 **GitHub Repository:** [https://github.com/Kowsalya-S-cse/AquaPredict-Pro](https://github.com/Kowsalya-S-cse/AquaPredict-Pro)

---

## 🌟 Key Capabilities

- **Precision Water Calculation**: Uses a trained Linear Regression model to calculate exact volumetric water requirements (in Liters) based on acreage and crop type.
- **Irrigation Efficiency Adjustment**: Accounts for drip, sprinkler, and flood irrigation efficiencies, computing real-time water savings.
- **Smart Agronomic Advice**: Dynamically provides actionable guidance (e.g. mulching, nocturnal watering schedules, soil aeration) based on humidity and temperature thresholds.
- **Resilient Direct Inference**: Integrated client-side model fallback ensures 100% cloud uptime even when the REST API backend is offline.

---

## 🏛️ System Architecture

```
+---------------------------------------------------------------------------------+
|                        1. STREAMLIT INTERACTIVE DASHBOARD                       |
|   - Crop & Soil Type Selectors (Rice, Wheat, Maize / Sandy, Clay, Loam)        |
|   - Real-Time Sliders: Temperature, Rainfall, Humidity, Acreage                |
|   - Efficiency Adjusted Water Metric Cards & Dynamic Agronomic Recommendations  |
+---------------------------------------------------------------------------------+
                                       ▲
                                       │ (REST / JSON / HTTP 5000)
                                       ▼
+---------------------------------------------------------------------------------+
|                              2. FLASK REST API                                  |
|   - Endpoint: POST /predict                                                     |
|   - Input Parsing & One-Hot Encoding Alignment (model_columns.pkl)             |
|   - Pre-loaded Linear Regression Inference Pipeline                             |
+---------------------------------------------------------------------------------+
                                       ▲
                                       │ (Serialized Weights)
                                       ▼
+---------------------------------------------------------------------------------+
|                        3. MACHINE LEARNING ENGINE                               |
|   - Model: Scikit-Learn LinearRegression                                        |
|   - Inputs: Rainfall, Temperature, Humidity, Soil Type, Crop Type, Acres        |
|   - Output: Recommended Water Requirement in Liters (Status 200)                |
+---------------------------------------------------------------------------------+
```

---

## 🚀 Quick Start Guide

### 1. Launch the Streamlit Frontend
```bash
cd frontend
pip install -r ../requirements.txt  # or: pip install streamlit requests pandas scikit-learn joblib
streamlit run frontend.py
```
Open `http://localhost:8501` to use the interactive dashboard.

### 2. Optional: Launch the Flask Backend API
```bash
cd backend
python app.py
```
Runs the REST API on `http://localhost:5000`.

---

## 📄 License
This project is open-source under the [MIT License](LICENSE).
