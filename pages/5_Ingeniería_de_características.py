import pandas as pd
import streamlit as st
import datetime as dt
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder


st.title('Ingeniería de características')
st.markdown('Se realizan transformaciones adicionales para trabajar mejor las \
    variables numéricas y las variables categóricas.')

train_df = st.session_state["train_df"]

st.header("Item_Type")
st.write("Se obtiene una nueva columna a partir de los primeros caracteres \
    de los códigos de Item_Identifier. Esta columna puede reemplazar a \
    Item_Type.")

# Item_Type group categorical variables
train_df["Item_Type_Id"] = train_df["Item_Identifier"].apply(lambda x: x[0:2])
# plot Item_Type_Id Bar chart horizontal
item_type_id_bar = go.Figure( go.Bar(
    y=train_df['Item_Type_Id'].value_counts().index,
    x=train_df['Item_Type_Id'].value_counts().values,
    marker_color='#5579C6',
    orientation='h'
    ))
item_type_id_bar.update_layout(title="Item Type Id",
                                xaxis_title="Item_Type_Id",
                                yaxis_title="Count")
st.plotly_chart(item_type_id_bar)

st.subheader("Outlet_Age")
st.write("Se obtiene una nueva columna a partir de la diferencia entre el \
    año actual y el año de apertura del establecimiento . Esta columna \
    puede reemplazar a Outlet_Age.")
# get outlet_age 
current_year =  dt.datetime.now().year
print(current_year)
train_df["Outlet_Age"] = current_year - train_df["Outlet_Establishment_Year"] 
# plot Outlet_Age bar chart
outlet_age_bar = go.Figure( go.Bar(
    x=train_df['Outlet_Age'].value_counts().index,
    y=train_df['Outlet_Age'].value_counts().values,
    marker_color='#5579C6'
    ))

outlet_age_bar.update_layout(title="Outlet Age",
                                xaxis_title="Outlet_Age",
                                yaxis_title="Count"
                            )
outlet_age_bar.update_xaxes(type='category')
st.plotly_chart(outlet_age_bar)

st.subheader("Variables Categóricas")
st.write("Se realizan transformaciones adicionales para trabajar mejor las \
    variables categóricas.")

st.write("Se codifican las variables categóricas.")
label = LabelEncoder()
print(train_df.columns)
vars_label_encoder = ['Item_Fat_Content', 'Outlet_Identifier',
        'Outlet_Size', 'Outlet_Location_Type',
       'Outlet_Type', 'Item_Type_Id'] 
for col in vars_label_encoder:
    train_df[col] = label.fit_transform(train_df[col])
st.table(train_df.head()[vars_label_encoder])
# get dummy variables

st.write("Se convierten las variables categóricas en variables binarias")
vars_dummy = ['Item_Fat_Content', 'Outlet_Identifier',
        'Outlet_Size', 'Outlet_Location_Type',
       'Outlet_Type', 'Item_Type_Id'] 
train_df = pd.get_dummies(train_df, columns=vars_dummy)
st.table(train_df.head())

st.session_state["train_df"] = train_df