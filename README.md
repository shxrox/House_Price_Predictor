# Ames House Price Prediction App

## Overview
This project is an end-to-end Machine Learning pipeline and interactive web application that predicts real estate house prices using the Ames Housing dataset. The model is trained on historical housing data and deployed as a Streamlit web app for real-time predictions.

🔗 Live Demo: https://shxrox-house-price-predictor-app-wonkze.streamlit.app/

---

## Features
- Predict house prices based on user input features
- Interactive web interface built with Streamlit
- End-to-end ML pipeline (data preprocessing → model training → prediction)
- Handles missing values and feature engineering
- Real-time inference
- Clean and user-friendly UI

---

## Dataset
The project uses the famous **Ames Housing Dataset**, which includes:
- Lot size
- House quality
- Year built
- Living area
- Number of rooms
- Garage and basement features
- And many more real estate attributes

---

## Tech Stack
- Python
- Pandas & NumPy
- Scikit-learn
- Matplotlib / Seaborn (for analysis)
- Streamlit (for web app)
- Joblib / Pickle (for model saving)

---

## Project Workflow
1. Data Collection
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Model Deployment (Streamlit App)

---

## Model Used
- Linear Regression / Random Forest / Gradient Boosting (depending on final implementation)
- Evaluation metrics:
  - RMSE
  - MAE
  - R² Score

---

## Installation

```bash
git clone https://github.com/your-username/ames-house-price-prediction.git
cd ames-house-price-prediction
pip install -r requirements.txt
streamlit run app.py
```

---

## Usage
1. Open the Streamlit web app
2. Enter house features (size, quality, rooms, etc.)
3. Click Predict
4. Get estimated house price instantly

---

## Project Structure
```
ames-house-price-prediction/
│
├── app.py
├── model.pkl
├── requirements.txt
├── data/
├── notebooks/
├── src/
└── README.md
```

---

## Deployment
The application is deployed using Streamlit Cloud:
👉 https://shxrox-house-price-predictor-app-wonkze.streamlit.app/

---

## Author
Developed as part of a Machine Learning portfolio project.

---

## License
This project is open-source and available under the MIT License.
