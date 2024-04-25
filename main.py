import streamlit as st
import requests
import plotly.express as px

st.title("Dashboard!")


ir_dashboard = "Ir al Dashboard"
url_dashboard = "https://jtmweah6cydnkwzrhhmxz8.streamlit.app/dashboard"

st.write("""# ¿Cómo pueden adaptarse las universidades al mercado IT?
## Tablero interactivo para la toma de decisiones


Desde la consultora **AVE** nos propusimos abordar una problemática actual determinada por los cambios frenéticos en los que nos encontramos envueltos como sociedad: el desarrollo tecnológico, la consecuente reconversión profesional y, sobre todo, el rol de la Universidad Tecnológica Nacional en este proceso.


Conscientes del rol que le toca a la Universidad en su papel de agente público clave para el desarrollo nacional, hemos decidido acercarles una herramienta que podría resultarles fundamental para afinar criterios a la hora de tomar decisiones: un **dashboard interactivo online** en el que podrán ingresar datasets estandarizados con información anual que les permitirá notar con claridad la evolución de determinadas métricas.


Dichas métricas emergen de los siguientes interrogantes, elementales para orientar el análisis hacia las decisiones más acertadas posibles:
¿Qué duración de cursado es más elegida en la actualidad? 
¿De qué profesión llegan más reconversiones al mundo IT?
¿Qué plataformas son las más elegidas? (nos sirve para utilizar su currícula como referencia)
¿Qué tipo de certificación son más elegidas?
¿Cuál es la situación laboral actual de las personas que eligen estudiar programación?
¿Cuál es la tasa de inserción laboral luego de obtener las certificaciones?
¿Cuántas certificaciones son necesarias para acceder al primer empleo?

Con estos interrogantes damos pie al análisis de datos en Excel, partiendo de la limpieza, verificación y comprensión de los mismos para la posterior elaboración de las visualizaciones en PowerBI.""")

st.image("/src/joel-filipe-Wc8k-KryEPM-unsplash.jpg", width=200, caption="Descripción de la primera imagen")

# Mostrar la segunda imagen con el mismo ancho
st.image("/src/andre-benz-cXU6tNxhub0-unsplash.jpg", width=200, caption="Descripción de la segunda imagen")

if st.button(ir_dashboard):
    # Redirigir al siguiente dashboard
    js = f"window.open('{url_dashboard}')"
    html = f'<img src onerror="{js}">'
    st.markdown(html, unsafe_allow_html=True)

