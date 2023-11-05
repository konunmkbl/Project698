import pickle
import pandas as pd
import streamlit as st

# Load the trained Random Forest model
with open('model.pkl', 'rb') as file:
    rf_model = pickle.load(file)

def predict_fraud(x_new):
    # Make predictions using the loaded model
    y_pred_new = rf_model.predict(x_new)
    return y_pred_new

st.title("Credit Card Fraud Prediction")

st.write("Enter the following information to predict credit card fraud:")

# Input fields for user to provide data
mcc = st.text_input("MCC (Merchant Category Code (4Digit)):")
zipcode = st.text_input("ZIP Code:")
currency = st.text_input("Currency:") 
st.write('1 = EUR / 2 = INR / 3 = USD')
card_type = st.text_input("Card Type:") 
st.write('1 = American Express / 2 = MasterCard / 3 = Visa')
device = st.text_input("Device:") 
st.write('1 = Desktop / 2 = Mobile / 3 = Tablet')

# Button to make predictions
if st.button("Predict Fraud"):
    try:
        # Create a DataFrame with user input
        x_new = pd.DataFrame({
            'MCC': [mcc],
            'ZIPCode': [zipcode],
            'Currency': [currency],
            'CardType': [card_type],
            'Device': [device]
        })

        # Make predictions
        result = predict_fraud(x_new)

        # Display the prediction
        if result[0] == 1:
            st.error("Flag Type is: Fraud")
        else:
            st.success("Flag Type is: Non-Fraud")
    except Exception as e:
        st.error(f"An error occurred: {e}")
