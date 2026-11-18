import streamlit as st
import requests
import time

# Page Configuration
st.set_page_config(
    page_title="💧 AquaPredict Pro", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Advanced Styling with Guaranteed High-Contrast Colors
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        /* Universal Text Contrast Enforcement */
        * {
            font-family: 'Inter', sans-serif;
            color-scheme: dark !important;
        }

        /* Global App Background */
        .stApp {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%) !important;
        }
        
        /* Hide Streamlit default chrome */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Header Hero */
        .hero-title {
            font-size: 3.2rem;
            font-weight: 800;
            background: linear-gradient(135deg, #10b981 0%, #38bdf8 50%, #06b6d4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-align: center;
            margin-bottom: 8px;
            letter-spacing: -0.02em;
        }
        
        .hero-subtitle {
            font-size: 1.25rem;
            color: #93c5fd !important;
            font-weight: 500;
            text-align: center;
            margin-bottom: 8px;
        }
        
        .hero-description {
            font-size: 1rem;
            color: #cbd5e1 !important;
            max-width: 650px;
            margin: 0 auto 35px auto;
            line-height: 1.6;
            text-align: center;
        }
        
        /* Section Headlines */
        .card-heading {
            font-size: 1.6rem !important;
            font-weight: 700 !important;
            color: #34d399 !important; /* Emerald Green */
            margin: 15px 0 20px 0 !important;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .column-heading {
            font-size: 1.25rem !important;
            font-weight: 700 !important;
            color: #38bdf8 !important; /* Electric Cyan */
            margin: 10px 0 4px 0 !important;
            text-shadow: 0 2px 4px rgba(0,0,0,0.4);
        }

        .column-subtext {
            color: #cbd5e1 !important;
            font-size: 0.9rem !important;
            margin-bottom: 18px !important;
        }

        /* Widget Labels (Rainfall, Crop Type, Acres, etc.) */
        label, 
        .stWidgetLabel, 
        [data-testid="stWidgetLabel"],
        [data-testid="stWidgetLabel"] *,
        [data-testid="stMarkdownContainer"] p {
            color: #ffffff !important;
            font-size: 1.05rem !important;
            font-weight: 600 !important;
            text-shadow: 0 1px 3px rgba(0,0,0,0.4);
        }

        /* Slider Value Displays & Tick Bars */
        div[data-testid="stTickBar"] div,
        div[data-testid="stSliderTickBar"] div,
        [data-testid="stThumbValue"] {
            color: #38bdf8 !important;
            font-weight: 600 !important;
        }

        /* Form Inputs (Selectbox & NumberInput) */
        .stSelectbox > div > div, 
        .stNumberInput > div > div {
            background-color: rgba(30, 41, 59, 0.9) !important;
            border: 2px solid rgba(71, 85, 105, 0.7) !important;
            border-radius: 12px !important;
            color: #ffffff !important;
        }

        div[data-baseweb="select"] *, 
        div[data-baseweb="input"] *,
        input {
            color: #ffffff !important;
            background-color: transparent !important;
            font-weight: 500 !important;
        }

        ul[data-baseweb="menu"] {
            background-color: #1e293b !important;
        }

        ul[data-baseweb="menu"] * {
            color: #ffffff !important;
        }

        /* Submit Button */
        .stButton > button {
            background: linear-gradient(135deg, #10b981 0%, #3b82f6 50%, #06b6d4 100%) !important;
            color: #ffffff !important;
            font-weight: 700 !important;
            font-size: 1.15rem !important;
            padding: 16px 45px !important;
            border: none !important;
            border-radius: 16px !important;
            box-shadow: 0 10px 25px -5px rgba(16, 185, 129, 0.5) !important;
            transition: all 0.3s ease !important;
            width: 100% !important;
            margin-top: 25px !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 15px 35px -5px rgba(16, 185, 129, 0.7) !important;
        }
        
        /* Result Highlights */
        .result-card {
            background: linear-gradient(135deg, #059669 0%, #2563eb 60%, #0284c7 100%) !important;
            color: #ffffff !important;
            padding: 35px !important;
            border-radius: 20px !important;
            text-align: center !important;
            margin: 30px 0 25px 0 !important;
            box-shadow: 0 15px 35px -5px rgba(16, 185, 129, 0.4) !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
        }
        
        .result-label {
            font-size: 1.3rem !important;
            font-weight: 600 !important;
            color: #e0f2fe !important;
            margin-bottom: 8px !important;
        }

        .result-value {
            font-size: 2.8rem !important;
            font-weight: 800 !important;
            color: #ffffff !important;
            margin: 12px 0 !important;
            text-shadow: 0 2px 10px rgba(0,0,0,0.3) !important;
        }
        
        .result-subtitle {
            font-size: 1.05rem !important;
            color: #f1f5f9 !important;
        }

        /* Streamlit Output Metrics Card */
        div[data-testid="stMetric"] {
            background: rgba(30, 41, 59, 0.85) !important;
            border: 1px solid rgba(71, 85, 105, 0.7) !important;
            padding: 18px 22px !important;
            border-radius: 16px !important;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3) !important;
        }

        div[data-testid="stMetricLabel"],
        div[data-testid="stMetricLabel"] * {
            color: #38bdf8 !important; /* Electric Cyan */
            font-size: 1.15rem !important;
            font-weight: 600 !important;
        }

        div[data-testid="stMetricValue"],
        div[data-testid="stMetricValue"] * {
            color: #ffffff !important; /* Bright White */
            font-size: 2.2rem !important;
            font-weight: 800 !important;
            text-shadow: 0 2px 8px rgba(0,0,0,0.4) !important;
        }

        /* Recommendation Section Title */
        .rec-heading {
            color: #34d399 !important; /* Emerald */
            font-size: 1.6rem !important;
            font-weight: 700 !important;
            margin: 35px 0 15px 0 !important;
        }

        /* Recommendation Alert Boxes */
        div[data-testid="stAlert"] {
            background: rgba(15, 23, 42, 0.9) !important;
            border: 1px solid rgba(56, 189, 248, 0.4) !important;
            border-radius: 14px !important;
            margin-bottom: 12px !important;
        }

        div[data-testid="stAlert"] p {
            color: #f8fafc !important;
            font-size: 1.02rem !important;
            font-weight: 500 !important;
        }
    </style>
""", unsafe_allow_html=True)


# Hero Section
st.markdown("""
    <div style="text-align: center; padding: 25px 0 10px 0;">
        <div class="hero-title">🌾 AquaPredict Pro</div>
        <div class="hero-subtitle">AI-Powered Water Management for Smart Agriculture</div>
        <div class="hero-description">
            Optimize your irrigation with precision agriculture technology. 
            Get accurate water requirement predictions based on real-time environmental data.
        </div>
    </div>
""", unsafe_allow_html=True)

# Main Section Card
st.markdown('<div class="card-heading">📊 Field Parameters</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="column-heading">🌤️ Weather Conditions</div>', unsafe_allow_html=True)
    st.markdown('<div class="column-subtext">Environmental factors affecting water needs</div>', unsafe_allow_html=True)
    rainfall = st.slider("🌧️ Rainfall (mm)", 0, 300, 120, help="Average rainfall in your area")
    temperature = st.slider("🌡️ Temperature (°C)", 0, 50, 30, help="Average temperature")
    humidity = st.slider("💧 Humidity (%)", 0, 100, 70, help="Relative humidity percentage")

with col2:
    st.markdown('<div class="column-heading">🌱 Crop Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="column-subtext">Specify your agricultural setup</div>', unsafe_allow_html=True)
    crop_type = st.selectbox(
        "🌾 Crop Type", 
        ["rice", "wheat", "maize", "sugarcane", "cotton"],
        help="Select your primary crop"
    )
    soil_type = st.selectbox(
        "🧱 Soil Type", 
        ["loam", "clay", "sandy", "silt"],
        help="Your soil composition"
    )

with col3:
    st.markdown('<div class="column-heading">📏 Field Specifications</div>', unsafe_allow_html=True)
    st.markdown('<div class="column-subtext">Area and irrigation details</div>', unsafe_allow_html=True)
    acres = st.number_input(
        "🌾 Field Area (acres)", 
        min_value=0.1, 
        value=1.0, 
        step=0.1,
        help="Total cultivated area"
    )
    irrigation_efficiency = st.slider(
        "💦 Irrigation Efficiency (%)", 
        60, 95, 80,
        help="Efficiency of your irrigation system"
    )

# Centered Predict Button
button_col1, button_col2, button_col3 = st.columns([1, 2, 1])
with button_col2:
    predict_clicked = st.button("🔮 Calculate Water Requirement", key="predict_btn")

if predict_clicked:
    prediction = None
    
    # 1. Attempt local Flask REST API if running
    try:
        url = "http://127.0.0.1:5000/predict"
        data = {
            "rainfall": rainfall,
            "temperature": temperature,
            "humidity": humidity,
            "soil_type": soil_type,
            "crop_type": crop_type,
            "acres": acres
        }
        resp = requests.post(url, json=data, timeout=1)
        if resp.status_code == 200:
            prediction = round(float(resp.json()["prediction_lr"]), 2)
    except Exception:
        pass

    # 2. Resilient Cloud Standalone ML Inference (Exact Linear Regression Coefficients)
    if prediction is None:
        try:
            intercept = -17.648457424334026
            soil_weights = {
                'clay': 6.988817097155811,
                'loam': -3.2534055959771884,
                'sandy': -0.1975460513063442,
                'silt': -3.5378654498722604
            }
            crop_weights = {
                'cotton': 1.3290760846119056,
                'maize': 2.456527984485232,
                'rice': 0.6640677189535459,
                'sugarcane': -4.605161969112909,
                'wheat': 0.1554901810622099
            }
            calc_val = (
                intercept +
                rainfall * 1.0087533956442842 +
                temperature * 0.5284550081154329 +
                humidity * -0.011547340859294764 +
                acres * 100.53297069750464 +
                soil_weights.get(soil_type.lower(), 0.0) +
                crop_weights.get(crop_type.lower(), 0.0)
            )
            prediction = round(float(calc_val), 2)
        except Exception as err:
            st.error(f"Inference error: {err}")

    if prediction is not None:
        # Adjust prediction based on irrigation efficiency
        adjusted_prediction = round(prediction * (100 / irrigation_efficiency), 2)
        water_saved = round(adjusted_prediction - prediction, 2)
        
        # Main Result Callout
        st.markdown(f"""
            <div class="result-card">
                <div class="result-label">💧 Recommended Water Requirement</div>
                <div class="result-value">{adjusted_prediction:,} L</div>
                <div class="result-subtitle">For {acres} acres of {crop_type.title()} with {irrigation_efficiency}% efficiency</div>
            </div>
        """, unsafe_allow_html=True)
        
        # 3 Key Metrics
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric(
                label="📈 Base Requirement",
                value=f"{prediction:,} L",
                help="Raw Linear Regression ML prediction"
            )
        with m2:
            st.metric(
                label="⚡ Efficiency Adjusted",
                value=f"{adjusted_prediction:,} L",
                delta=f"+{water_saved} L",
                help="Adjusted for field irrigation efficiency"
            )
        with m3:
            daily_req = round(adjusted_prediction / 7, 2)
            st.metric(
                label="📅 Daily Average",
                value=f"{daily_req:,} L",
                help="Estimated daily irrigation demand"
            )
            
        # Agronomic Recommendations
        st.markdown('<div class="rec-heading">💡 Smart Agronomic Recommendations</div>', unsafe_allow_html=True)
        recommendations = []
        if humidity < 50:
            recommendations.append("🌡️ **Low humidity detected**: Apply organic mulching to suppress soil water evaporation.")
        if temperature > 35:
            recommendations.append("🔥 **High temperature advisory**: Shift irrigation cycles to early morning or late evening.")
        if rainfall > 200:
            recommendations.append("🌧️ **Heavy rainfall expected**: Postpone automated irrigation to avoid soil waterlogging.")
        if soil_type.lower() == "sandy":
            recommendations.append("🏖️ **Sandy soil composition**: High percolation rate — distribute water in smaller, frequent intervals.")
        if irrigation_efficiency < 75:
            recommendations.append("💧 **Low irrigation efficiency**: Upgrade to localized drip irrigation to conserve up to 35% water.")
            
        if recommendations:
            for rec in recommendations:
                st.info(rec)
        else:
            st.success("✅ Environmental and crop parameters are optimal for balanced irrigation!")

# Footer
st.markdown("""
    <div style="text-align: center; margin-top: 55px; padding: 25px; color: #94a3b8; border-top: 1px solid rgba(71, 85, 105, 0.3);">
        <p>🌱 <strong>AquaPredict Pro</strong> • AI-Powered Sustainable Precision Agriculture</p>
    </div>
""", unsafe_allow_html=True)
