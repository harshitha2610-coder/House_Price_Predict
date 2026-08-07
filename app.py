import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("house_price_tree_model.pkl")

# Page settings
st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 House Price Prediction System")
st.write("Enter the house details below to predict the price.")

# Input fields
area = st.number_input("Area (sq.ft)", min_value=500, max_value=10000, value=1500)

bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)

bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)

floors = st.number_input("Floors", min_value=1, max_value=5, value=2)

yearbuilt = st.number_input("Year Built", min_value=1900, max_value=2025, value=2015)

location = st.number_input(
    "Location Code (0=Downtown, 1=Suburban, 2=Urban)",
    min_value=0,
    max_value=2,
    value=0
)

condition = st.number_input(
    "Condition Code (0=Poor, 1=Average, 2=Good)",
    min_value=0,
    max_value=2,
    value=2
)

garage = st.number_input(
    "Garage Code (0=No, 1=Yes)",
    min_value=0,
    max_value=1,
    value=1
)

# Predict
if st.button("Predict Price"):

    features = np.array([[area,
                          bedrooms,
                          bathrooms,
                          floors,
                          yearbuilt,
                          location,
                          condition,
                          garage]])

    prediction = model.predict(features)

    st.success(f"🏠 Estimated House Price: ₹ {prediction[0]:,.2f}")