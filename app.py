import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the trained model
with open("lgbm_model.pkl", "rb") as f:
    model = pickle.load(f)

# Function to take user input
def input_data():
    bhk = st.slider(label='BHK', min_value=1, max_value=6, step=1)
    city = st.selectbox('City', ('Kolkata', 'Mumbai', 'Bangalore', 'Delhi', 'Chennai', 'Hyderabad'))
    furn_s = st.selectbox('Furnishing Status', ('Unfurnished', 'Semi-Furnished', 'Furnished'))
    tenant = st.selectbox('Tenant Preferred', ('Bachelors/Family', 'Bachelors', 'Family'))
    bath = st.slider(label='Bathroom', min_value=1, max_value=7, step=1)
    point_c = st.selectbox('Point of Contact', ('Contact Owner', 'Contact Agent'))
    rent = st.slider(label='Rental Floor', min_value=-2, max_value=22, step=1)
    total_f = st.slider(label='Total Number of Floor', min_value=0, max_value=30, step=1)
    fixed_s = st.slider(label="Fixed Size (Sqft)", min_value=10, max_value=3100, step=10)
    square_feet_rent = st.slider(label="Square Feet Rent", min_value=10, max_value=120, step=2)

    columns = [
        'BHK', 'City', 'Furnishing Status', 
        'Tenant Preferred','Bathroom', 'Point of Contact',
        'Rental Floor', 'Total Number of Floor','Fixed Size', "Square Feet Rent"
    ]
    new_data = [[bhk, city, furn_s, tenant, bath, point_c, rent, total_f, fixed_s, square_feet_rent]]
    return pd.DataFrame(new_data, columns=columns)

# Prediction logic
def predict():
    st.title("🏠 Apartment Rent Prediction App")
    st.subheader("Enter apartment details to get the estimated rent:")

    new_data = input_data()

    if st.button('Predict Rent'):
        prediction = model.predict(new_data)
        st.success(f'Estimated Rent (INR): ₹ {np.round(prediction[0], 2)}')

# Run the app
if __name__ == "__main__":
    predict()
