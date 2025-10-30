Clone the repository

git clone https://github.com/Vijayashree-tech/AIDC-pro.git
cd AIDC-pro


Install dependencies

pip install -r requirements.txt


Run the Streamlit app

streamlit run app.py


Open the browser at the URL shown (usually http://localhost:8501
)

⚙️ Backend (Flask API)

Clone the repository

git clone https://github.com/Kowsalya-S-cse/crop-water-prediction.git
cd crop-water-prediction


Install dependencies

pip install -r requirements.txt


Run the Flask server

python app.py


The backend will start on http://127.0.0.1:5000

🌐 Integration Notes

Ensure both frontend and backend are running simultaneously.

The Streamlit frontend communicates with the Flask backend API for predictions.

Update the API endpoint in the frontend code if necessary (e.g., inside app.py → change the URL to match the Flask server address).
