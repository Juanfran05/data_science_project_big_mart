import pandas as pd
import numpy as np
import streamlit as st

from utils.import_data import import_train_data
from utils.explore_data import profile_data

st.title("Exploración inicial 📊")

st.header("Train data")
st.write("Se presenta el anális exploratorio a partir de pandas profiling.")
train_df = import_train_data()
profile_data(train_df)

st.header("Observaciones")
st.markdown("""
- Item_Identifier cuenta con alta cardinalidad. Se observa que un mismo item se repite hasta 10 veces, probablemente porque se vende hasta en 10 tiendas distintas.

- Item_Weight cuenta con el 17.2% de datos faltantes, por lo que se trabajará en completar la información.

- Item_Fat_Content tiene problemas con las etiquetas de los datos, estas no están estandarizadas.

- Item_Visibility cuenta con un 6.2% de zeros y además tiene una distribución asimétrica con cola a la derecha. Este atributo puede normalizarse.

- Item_Type cuenta con 16 categorías. Se intentará agrupar las categorías para disminuir su número y mejorar el rendimiento de la predicción.

- Item_MRP tiene una alta correlación (Pearson y Phik ) con Item_Outlet_Sales

- Outlet_Identifier tiene una alta correlación (Phik) con Item_Outlet_Sales

- Outlet_Establishment_Year requiere ser transformada a años de antigüedad de la tienda.

- Outlet_Size contiene un 28.3% de datos faltantes

- Outlet_Location_Type sin comentarios

- Outlet_Type sin comentarios

- Item_Outlet_Sales será la variable objetivo a predecir.

""")
