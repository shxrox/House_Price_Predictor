import streamlit as st
import pandas as pd
import joblib


model = joblib.load('house_model.pkl')


st.title("🏡 Real Estate AI Predictor")
st.write("Adjust the features below to predict the final sale price of a house.")


col1, col2 = st.columns(2)

with col1:
 
    overall_qual = st.slider("Overall Quality (1-10)", min_value=1, max_value=10, value=5)
    gr_liv_area = st.number_input("Living Area (sq ft)", min_value=500, max_value=6000, value=1500)
    garage_cars = st.number_input("Garage Size (Cars)", min_value=0, max_value=5, value=2)

with col2:
    total_bsmt_sf = st.number_input("Basement Size (sq ft)", min_value=0, max_value=5000, value=1000)
    full_bath = st.number_input("Full Bathrooms", min_value=1, max_value=5, value=2)
    year_built = st.number_input("Year Built", min_value=1800, max_value=2026, value=2000)



if st.button("Predict Price"):
    
   
    input_data = pd.DataFrame({
        'OverallQual': [overall_qual],
        'GrLivArea': [gr_liv_area],
        'GarageCars': [garage_cars],
        'TotalBsmtSF': [total_bsmt_sf],
        'FullBath': [full_bath],
        'YearBuilt': [year_built]
    })

    
    prediction = model.predict(input_data)[0]

    
    st.success(f"Estimated House Price: ${prediction:,.2f}")