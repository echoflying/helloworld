import os
import streamlit as st

is_on_streamlit_cloud = 'STREAMLIT_CLOUD' in os.environ

st.header("Hello World")

if is_on_streamlit_cloud:
    st.write("Running on Streamlit Cloud.")
else:
    st.write("Not running on Streamlit Cloud.")

    