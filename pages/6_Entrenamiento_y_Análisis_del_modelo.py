import streamlit as st
import pandas as pd


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from utils.fit_model import modelos

st.title('Entrenamiento y análisis del modelo')
st.markdown('Se seleccionarán las variables a utilizar y se realizará un\
    análisis del rendimiento del modelo.')
train_df = st.session_state["train_df"]

cols_for_model = ['Item_Weight', 'Item_Visibility','Item_MRP',
        'Outlet_Age', 'Item_Fat_Content_0',
       'Item_Fat_Content_1', 'Outlet_Identifier_0', 'Outlet_Identifier_1',
       'Outlet_Identifier_2', 'Outlet_Identifier_3', 'Outlet_Identifier_4',
       'Outlet_Identifier_5', 'Outlet_Identifier_6', 'Outlet_Identifier_7',
       'Outlet_Identifier_8', 'Outlet_Identifier_9', 'Outlet_Size_0',
       'Outlet_Size_1', 'Outlet_Size_2', 'Outlet_Location_Type_0',
       'Outlet_Location_Type_1', 'Outlet_Location_Type_2', 'Outlet_Type_0',
       'Outlet_Type_1', 'Outlet_Type_2', 'Outlet_Type_3', 'Item_Type_Id_0',
       'Item_Type_Id_1', 'Item_Type_Id_2']
target = 'Item_Outlet_Sales'

st.write("Tomando en cuenta los coeficientes de correlación de Phik se establece que las variables \
        a utilizar son:")
st.write(cols_for_model)

st.write("Se realiza una división de los datos en train y val.")
X = train_df[cols_for_model]
y = train_df[target]
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2,
    random_state=1) #stratify=y
st.write("X_train_shape: {}, X_val_shape: {}".format(X_train.shape, X_val.shape))
st.write("y_train_shape: {}, y_val_shape: {}".format(y_train.shape, y_val.shape))

st.write("Se entrena el modelo y se obtienen los coeficientes.")
lr = LinearRegression()
coeficientes, fig1, fig2, values = modelos(X_val, y_val, X_train, y_train, lr, "lineal")
st.write(coeficientes)
st.write("Se observa el rendimiento del modelo mediante indicadores y gráficas.")
st.write(values)
st.plotly_chart(fig1)
st.plotly_chart(fig2)

st.subheader("Observaciones")
st.write("Se observa que el modelo tiene un r2 bastante bajo, lo que genera mucha \
    desconfianza en los valores que predice. Se probó con modelos de Ridge, Lasso, \
        AdaBoost y Random Forest pero se obtuvieron resultados incluso con menor r2")
st.write("Los parámetros más importantes del modelo son Outlet_Type y Outlet_Identifier \
    lo que indica que el tipo de distribuidor y el distribuidor en sí mismos son \
        los agentes más importantes para el rendimiento de las ventas del producto.")

st.session_state["regression_model"] = lr
st.session_state["cols_for_model"] = cols_for_model