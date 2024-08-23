import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(file):
    data = file.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

uploaded_file = st.file_uploader("Upload an image", type="jpg")

if uploaded_file is not None:
    if st.button('Generate Caption'):
        output = query(uploaded_file)
        st.json(output)
else:
    st.text("Please upload a JPG image.")
