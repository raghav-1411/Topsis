import smtplib
from email.message import EmailMessage
import streamlit as st

def send_email(receiver_email, file_path):
    sender_email = st.secrets["EMAIL"]
    sender_password = st.secrets["EMAIL_PASSWORD"]

    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result File"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Please find the attached TOPSIS result file.")

    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="topsis_result.csv"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)
