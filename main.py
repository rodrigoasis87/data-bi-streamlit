import streamlit as st
import requests
import plotly.express as px

st.title("Dashboard!")


ir_dashboard = "Ir al Dashboard"
url_dashboard = "https://jtmweah6cydnkwzrhhmxz8.streamlit.app/dashboard"




if st.button(ir_dashboard):
    # Redirigir al siguiente dashboard
    js = f"window.open('{url_dashboard}')"
    html = f'<img src onerror="{js}">'
    st.markdown(html, unsafe_allow_html=True)

