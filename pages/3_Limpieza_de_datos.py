import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go

from utils.import_data import import_train_data

st.title("Limpieza de datos 🧐")

train_df = import_train_data()

st.header("Item_Weight")
st.write("Se reemplazaron datos faltantes por la media.")
# Item_Weight fillna with median
train_df['Item_Weight'].fillna(train_df['Item_Weight'].median(), inplace=True)

#plot Item_Weight histogram
item_weight_histogram = go.Figure( go.Histogram(
    x=train_df['Item_Weight'],
    marker_color='#5579C6'
    ))
item_weight_histogram.update_layout(title="Item Weight Histogram",
                                xaxis_title="Item_Weight",
                                yaxis_title="Count")
st.plotly_chart(item_weight_histogram)

#plot Item_Weight boxplot
item_weight_boxplot = go.Figure( go.Box(
    x=train_df['Item_Weight'],
    marker_color='#5579C6'
    ))
item_weight_boxplot.update_layout(title="Item Weight Boxplot")
st.plotly_chart(item_weight_boxplot)


st.header("Item_Fat_Content")
st.write("Se renombraron las etiquetas para encajarlas en las dos categorías existentes.")
# Item_Fat_Content rename categorical variable
train_df.replace({"Item_Fat_Content": {"low fat": "Low Fat", "Low Fat": "Low Fat", "reg": "Regular", "Regular": "Regular", "reg ": "Regular", "LF": "Low Fat"}} , inplace=True)
#plot Item_Fat_Content Bar chart horizontal
item_fat_content_bar = go.Figure( go.Bar(
    y=train_df['Item_Fat_Content'].value_counts().index,
    x=train_df['Item_Fat_Content'].value_counts().values,
    marker_color='#5579C6',
    orientation='h'
    ))
item_fat_content_bar.update_layout(title="Item Fat Content",
                                xaxis_title="Item_Fat_Content",
                                yaxis_title="Count")
st.plotly_chart(item_fat_content_bar)

st.header("Item_Visibility")
st.write("Se reemplazó los datos faltantes por el promedio de visibilidad del producto en otras tiendas.")
# Item_Visibility average group by Item_Identifier
train_df['Item_Visibility_avg'] = train_df.groupby('Item_Identifier')['Item_Visibility'].transform('mean')
# plot Item_Visibility_avg histogram
item_visibility_avg_histogram = go.Figure( go.Histogram(
    x=train_df['Item_Visibility_avg'],
    marker_color='#5579C6'
    ))
item_visibility_avg_histogram.update_layout(title="Item Visibility Avg Histogram",
                                xaxis_title="Item_Visibility_avg",
                                yaxis_title="Count")
st.plotly_chart(item_visibility_avg_histogram)
# Item_Visibility
item_visibility_avg = train_df.groupby("Item_Identifier").mean()["Item_Visibility"] 
train_df['Item_Visibility'] = train_df.apply(lambda x: item_visibility_avg[x["Item_Identifier"]] if x["Item_Visibility"] ==0 else x["Item_Visibility"], axis=1)
# plot Item_Visibility_new histogram
item_visibility_new_histogram = go.Figure( go.Histogram(
    x=train_df['Item_Visibility'],
    marker_color='#5579C6'
    ))
item_visibility_new_histogram.update_layout(title="Item Visibility Histogram",
                                xaxis_title="Item_Visibility",
                                yaxis_title="Count")
st.plotly_chart(item_visibility_new_histogram)


st.header("Outlet_Size")
st.write("Se reemplazaron los valores nullos por la moda según el outlet_type")

# Outlet_Size fillna with mode by outler_type
outlet_size_mode = train_df.pivot_table(values='Outlet_Size',
      columns='Outlet_Type',aggfunc=lambda x:x.mode())
print(outlet_size_mode)

train_df["Outlet_Size"].fillna("None", inplace=True)
train_df["Outlet_Size"] = train_df.apply(lambda x: outlet_size_mode.loc['Outlet_Size'][x["Outlet_Type"]] if x["Outlet_Size"] == "None" else x["Outlet_Size"], axis=1)

#plot Outlet_Size Bar chart horizontal
outlet_size_bar = go.Figure( go.Bar(
    y=train_df['Outlet_Size'].value_counts().index,
    x=train_df['Outlet_Size'].value_counts().values,
    marker_color='#5579C6',
    orientation='h'
    ))
outlet_size_bar.update_layout(title="Outlet Size",
                                xaxis_title="Outlet_Size",
                                yaxis_title="Count")
st.plotly_chart(outlet_size_bar)

st.session_state["train_df"] = train_df