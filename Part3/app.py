import streamlit as st
import pandas as pd
import re
from topsis_logic import run_topsis
from utils.email_service import send_email

st.set_page_config(page_title="TOPSIS Web Service")

st.title("TOPSIS Web Service")
st.write("Upload CSV, enter weights & impacts, and receive result via email")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
weights = st.text_input("Weights (comma separated)", "1,1,1,1")
impacts = st.text_input("Impacts (comma separated)", "+,+,-,+")
email = st.text_input("Email ID")

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

if st.button("Submit"):
    try:
        if not uploaded_file:
            st.error("Please upload a CSV file")
        elif not is_valid_email(email):
            st.error("Invalid email format")
        else:
            df = pd.read_csv(uploaded_file)
            result = run_topsis(df, weights, impacts)
            result.to_csv("output.csv", index=False)

            send_email(email, "output.csv")

            st.success("TOPSIS analysis completed and email sent successfully!")
            st.dataframe(result)

    except Exception as e:
        st.error(str(e))
