
import streamlit as st
import pandas as pd
import pickle

# Load your trained model
with open('your_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title("Customer Churn Prediction")

# Input fields for user data
st.header("Input Customer Data")

# Input fields corresponding to your features
credit_score = st.number_input("Credit Score", min_value=300, max_value=850)
geography = st.selectbox("Geography", options=["France", "Spain", "Germany"])
gender = st.selectbox("Gender", options=["Male", "Female"])
age = st.number_input("Age", min_value=18, max_value=100)
tenure = st.number_input("Tenure (Years)", min_value=0, max_value=10)
balance = st.number_input("Balance", min_value=0.0)
num_of_products = st.number_input("Number of Products", min_value=1, max_value=4)
has_cr_card = st.number_input("Has Credit Card (1 for Yes, 0 for No)", min_value=0, max_value=1)
is_active_member = st.number_input("Is Active Member (1 for Yes, 0 for No)", min_value=0, max_value=1)
estimated_salary = st.number_input("Estimated Salary", min_value=0.0)

# Convert categorical inputs to numeric
geography_map = {"France": 1, "Spain": 2, "Germany": 0}
gender_map = {"Male": 1, "Female": 0}


# Create a DataFrame to hold the input data
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Geography': [geography_map[geography]],
    'Gender': [gender_map[gender]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],

    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})

# Button to predict
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write("Churn Prediction (Exited):", prediction[0])
    if prediction[0] == 1:
        st.success("This customer is likely to churn.")
    else:
        st.success("This customer is likely to stay.")

st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line for separation
st.markdown("Made by Aakansha © 2024", unsafe_allow_html=True)
