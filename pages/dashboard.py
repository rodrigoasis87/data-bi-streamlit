import streamlit as st

url_informe_power_bi = "https://app.powerbi.com/view?r=eyJrIjoiNWIwMjI2NmMtZDk5ZS00NDI5LWJjZmQtODNhOTFiNmYxYTdhIiwidCI6IjA3NjBkZWZkLTgzODEtNGU5OS05Mjk2LTliOWU1MGM2NTRmNyIsImMiOjR9"
st.markdown(f'<iframe width="800" height="600" src="{url_informe_power_bi}"></iframe>', unsafe_allow_html=True)