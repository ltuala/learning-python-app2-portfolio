import smtplib, ssl
import streamlit as st

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "lyndontuala@gmail.com"
    password = st.secrets["PASSWORD"]
    receiver = "lyndontuala@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
