import streamlit as st
from parser import parse_resume

st.title("AI Resume Parser 🔥")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded_file:
    st.write("Processing...")

    try:
        data = parse_resume(uploaded_file)
        st.json(data)
    except Exception as e:
        st.error(f"Error: {e}")
