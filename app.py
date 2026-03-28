import streamlit as st
from parser import parse_resume

st.title("AI Resume Parser 🔥")

uploaded_file = st.file_uploader("Upload Resume")

if uploaded_file:
    data = parse_resume(uploaded_file)
    st.json(data)