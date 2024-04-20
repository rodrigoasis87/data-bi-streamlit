import streamlit as st
import requests
import base64
import plotly.express as px

# df = px.data.iris()

# @st.cache_data
# def get_experimental_base64(file):
#     with open(file, "rb") as f:
#         data = f.read()
#     return base64.b64decode(data).decode()

# img = get_experimental_base64("")

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image:  url("https://images.unsplash.com/photo-1493514789931-586cb221d7a7?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&dl=andre-benz-cXU6tNxhub0-unsplash.jpg");
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

st.sidebar.header("Menú")
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Dashboard!")


# st.markdown(
#     global_css,
#     unsafe_allow_html=True
# )


# def main():
#     st.markdown('<style>body { background-color: #fafafa; }</style>', unsafe_allow_html=True)
#     # Agrega el resto de tu aplicación Streamlit aquí
#     st.title('Mi aplicación con imagen de fondo')
#     st.write('¡Hola, mundo!')

# if __name__ == '__main__':
#     main()

