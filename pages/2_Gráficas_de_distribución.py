import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go

from utils.import_data import import_train_data

st.title("Gráficas de distribución 📊")

train_data = import_train_data()

#graph every colum on train data

# graph Item_Identifier
st.header("Item Identifier")
item_identifier_graph = go.Figure( go.Bar(
    y=train_data['Item_Identifier'].value_counts().index,
    x=train_data['Item_Identifier'].value_counts().values,
    marker_color='#5579C6',
    orientation='h'
    ))
item_identifier_graph.update_layout(title="Item Identifier", 
                                    xaxis_title="Item_Identifier",
                                    yaxis_title="Count")
st.plotly_chart(item_identifier_graph)
