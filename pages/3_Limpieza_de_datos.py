import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go

from utils.import_data import import_train_data

st.title("Limpieza de datos 🧐")

train_data = import_train_data()

#graph item_fat_content
st.header("Item fat content")
item_fat_content_graph = go.Figure( go.Bar(
    x=train_data['Item_Fat_Content'].value_counts().index,
    y=train_data['Item_Fat_Content'].value_counts().values,
    marker_color='#5579C6'
    ))
item_fat_content_graph.update_layout(title="Item fat content - Original",
                                     xaxis_title="Item_Fat_Content",
                                     yaxis_title="Count")    
# color_blue_light = '#00ff00'
st.plotly_chart(item_fat_content_graph)
st.markdown("The Item fat content necesita estandarizar/renombrar las categorías.")

item_fat_content_clean = train_data['Item_Fat_Content'].replace(['LF','low fat','reg','low fat'],['Low Fat','Low Fat','Regular','Regular'])
item_fat_content_clean_graph = go.Figure( go.Bar(
    x=item_fat_content_clean.value_counts().index,
    y=item_fat_content_clean.value_counts().values,
    marker_color='#5579C6'
))
item_fat_content_clean_graph.update_layout(title="Item fat content - Clean",
                                        xaxis_title="Item_Fat_Content",
                                        yaxis_title="Count")
st.plotly_chart(item_fat_content_clean_graph)

# st.header("Item visibility")
# item visibility histogram
# item_visibility_hist = go.Figure( go.Histogram(
#     x=train_data['Item_Visibility'],
#     marker_color='#5579C6'
# ))


# item_visibility_hist.update_layout(title="Item visibility - Original",
#                                         xaxis_title="Item_Visibility_", 
#                                         yaxis_title="Count")
# st.plotly_chart(item_visibility_hist)



