import streamlit as st
import requests
import plotly.express as px



url_informe_power_bi = "https://app.powerbi.com/view?r=eyJrIjoiNWIwMjI2NmMtZDk5ZS00NDI5LWJjZmQtODNhOTFiNmYxYTdhIiwidCI6IjA3NjBkZWZkLTgzODEtNGU5OS05Mjk2LTliOWU1MGM2NTRmNyIsImMiOjR9"
ir_dashboard = "Ir al Dashboard"


st.title("Dashboard!")
#st.components.html(f'<iframe title="NoCountry" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiODE2MjVmOGMtMjRjYi00ZDUxLTgyOGYtMzQwMmM5M2I0OTkwIiwidCI6IjA3NjBkZWZkLTgzODEtNGU5OS05Mjk2LTliOWU1MGM2NTRmNyIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>', height=800)
st.markdown(f'<iframe width="800" height="600" src="{url_informe_power_bi}"></iframe>', unsafe_allow_html=True)

st.sidebar.title("Menú")
st.sidebar.markdown("")

if st.button("Ir al Dashboard"):
    # Redirigir al siguiente dashboard
    st.markdown("[Siguiente página](/home/rodrigoasis87/c17-81-m-data-bi/pages/dashboard.py)")

