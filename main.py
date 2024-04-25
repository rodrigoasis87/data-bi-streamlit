import streamlit as st
import requests
import plotly.express as px

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1493514789931-586cb221d7a7?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&dl=andre-benz-cXU6tNxhub0-unsplash.jpg");
background-size: cover;
}

[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}

[data-testid="stToolbar"] {
right: 2rem;
}

[data-testid="stSidebar"] {
background-color: #e5e5f7;
opacity: 0.8;
background-image:  linear-gradient(#444cf7 1px, transparent 1px), linear-gradient(to right, #444cf7 1px, #e5e5f7 1px);
background-size: 20px 20px;
}


</style>
"""
url_informe_power_bi = "https://app.powerbi.com/view?r=eyJrIjoiNWIwMjI2NmMtZDk5ZS00NDI5LWJjZmQtODNhOTFiNmYxYTdhIiwidCI6IjA3NjBkZWZkLTgzODEtNGU5OS05Mjk2LTliOWU1MGM2NTRmNyIsImMiOjR9"

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Dashboard!")
st.markdown(f'<iframe width="800" height="600" src="{url_informe_power_bi}"></iframe>', unsafe_allow_html=True)

st.sidebar.title("Menú")
st.sidebar.markdown("")

if st.button("Ir al Dashboard"):
    # Redirigir al siguiente dashboard
    st.markdown("[Siguiente página](/home/rodrigoasis87/c17-81-m-data-bi/pages/dashboard.py)")

