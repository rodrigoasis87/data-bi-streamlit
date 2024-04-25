import streamlit as st
import requests
import plotly.express as px

st.title("Dashboard!")

url_informe_power_bi = "https://app.powerbi.com/view?r=eyJrIjoiNWIwMjI2NmMtZDk5ZS00NDI5LWJjZmQtODNhOTFiNmYxYTdhIiwidCI6IjA3NjBkZWZkLTgzODEtNGU5OS05Mjk2LTliOWU1MGM2NTRmNyIsImMiOjR9"
ir_dashboard = "Ir al Dashboard"

#st.components.html(f'<iframe title="NoCountry" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiODE2MjVmOGMtMjRjYi00ZDUxLTgyOGYtMzQwMmM5M2I0OTkwIiwidCI6IjA3NjBkZWZkLTgzODEtNGU5OS05Mjk2LTliOWU1MGM2NTRmNyIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>', height=800)
st.markdown(f'<iframe width="800" height="600" src="{url_informe_power_bi}"></iframe>', unsafe_allow_html=True)


if st.button(ir_dashboard):
    # Redirigir al siguiente dashboard
    js = f"window.open('{url_informe_power_bi}')"
    html = f'<img src onerror="{js}">'
    st.markdown(html, unsafe_allow_html=True)

