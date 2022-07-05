import streamlit as st
from PIL import Image

st.title("Home page 🌟")

st.header("Bienvenido a BigMart Sales App 🧑‍🚀")

st.markdown("Esta aplicación es un dashboard de Streamlit que ayuda a \
    explorar y realizar análisis de datos en el dataset de BigMart.")


st.markdown("El respositorio de esta app está disponible en [github](https://github.com/Juanfran05/data_science_project_big_mart/tree/main).")


# def main_page():
#     st.markdown("# Main page 🎈")
#     st.sidebar.markdown("# Main page 🎈")

# def page2():
#     st.markdown("# Page 2 ❄️")
#     st.sidebar.markdown("# Page 2 ❄️")

# def page3():
#     st.markdown("# Page 3 🎉")
#     st.sidebar.markdown("# Page 3 🎉")

# page_names_to_funcs = {
#     "Main Page": main_page,
#     "Page 2": page2,
#     "Page 3": page3,
# }

# selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
# page_names_to_funcs[selected_page]()