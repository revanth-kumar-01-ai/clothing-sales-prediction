import streamlit as st 
import json
import requests
import pandas as pd 

st.header("🛒 Clothing Sales Prediction - User Input")

# Function for One-Hot Encoding
def encode_category(value, options):
    return [1 if value == opt else 0 for opt in options[:-1]]  # Drop last category

# Create three columns
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    # Categorical Inputs
    shelve_loc = st.selectbox("📌 Select Shelve Location", ["Good", "Medium", "Bad"])
    urban = st.selectbox("🏙️ Urban Area?", ["Yes", "No"])
    us = st.selectbox("🇺🇸 Customer in the US?", ["Yes", "No"])

with col2:
    # Numerical Inputs - Part 1
    comp_price = st.number_input("💲 Competitor's Price", min_value=0.0, step=1.0)
    income = st.number_input("💰 Customer's Income", min_value=0.0, step=1.0)
    advertising = st.number_input("📢 Advertising Budget", min_value=0.0, step=1.0)
    population = st.number_input("🌍 Population", min_value=0.0, step=1.0)

with col3:
    # Numerical Inputs - Part 2
    price = st.number_input("🏷️ Product Price", min_value=0.0, step=1.0)
    age = st.number_input("🎂 Customer's Age", min_value=0, step=1)
    education = st.number_input("🎓 Education Level", min_value=0, step=1)

# Apply Encoding
shelve_loc_good, shelve_loc_medium = encode_category(shelve_loc, ["Good", "Medium", "Bad"])
urban_yes, = encode_category(urban, ["Yes", "No"])
us_yes, = encode_category(us, ["Yes", "No"])

# Create a dictionary for JSON conversion
user_inputs_dict = {
    "ShelveLoc_Good": shelve_loc_good,
    "ShelveLoc_Medium": shelve_loc_medium,
    "Urban_Yes": urban_yes,
    "US_Yes": us_yes,
    "CompPrice": comp_price,
    "Income": income,
    "Advertising": advertising,
    "Population": population,
    "Price": price,
    "Age": age,
    "Education": education
}

# Convert dictionary to JSON
user_inputs_json = json.dumps(user_inputs_dict, indent=4)

# Function to send API request
def cloth_sales_prediction(url, data):
    try:
        with st.spinner("🔄 Predicting... Please wait"):  # Show spinner
            response = requests.post(url, json=data)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx, 5xx)

            result = response.json()
            return result

    except requests.exceptions.RequestException as e:
        st.error(f"❌ Prediction failed: {e}")  # Show error in UI
        return None

# Submit Button
if st.button("🔍 Predict"):
    st.subheader("🔹 Selected & Encoded Values (JSON)")
    st.table(pd.DataFrame([user_inputs_dict]))

    # Call API and display results
    url = "https://ml-models-app.onrender.com/cloth_sales"
    prediction_result = cloth_sales_prediction(url, user_inputs_dict)

    if prediction_result:
        st.success("✅ Prediction Successful!")
        st.subheader("📊 Prediction Result")
        st.write(prediction_result)
