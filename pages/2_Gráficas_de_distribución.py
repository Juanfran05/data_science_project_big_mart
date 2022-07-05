import pandas as pd
import streamlit as st
import plotly.graph_objects as go

from utils.import_data import import_train_data

st.title("Gráficas de distribución 📊")

train_df = import_train_data()

#graph every colum on train data

# graph Item_Identifier
item_identifier_graph = go.Figure( go.Bar(
    y=train_df['Item_Identifier'].value_counts().index,
    x=train_df['Item_Identifier'].value_counts().values,
    marker_color='#5579C6',
    orientation='h'
    ))
item_identifier_graph.update_layout(title="Item Identifier", 
                                    yaxis_title="Item_Identifier",
                                    xaxis_title="Count")
st.plotly_chart(item_identifier_graph)

#plot Item_Weight Histogram
item_weight_graph = go.Figure( go.Histogram(
    x=train_df['Item_Weight'],
    marker_color='#5579C6'
    ))
item_weight_graph.update_layout(title="Item Weight Histogram",
                                xaxis_title="Item_Weight",
                                yaxis_title="Count")
st.plotly_chart(item_weight_graph)

#plot Item_Weight Boxplot horizontal
item_weight_boxplot = go.Figure( go.Box(
    x=train_df['Item_Weight'],
    marker_color='#5579C6',
    ))
item_weight_boxplot.update_layout(title="Item Weight Boxplot")
st.plotly_chart(item_weight_boxplot)

#plot Item_Fat_Content Bar Chart
item_fat_content_graph = go.Figure( go.Bar(
    y=train_df['Item_Fat_Content'].value_counts().index,
    x=train_df['Item_Fat_Content'].value_counts().values,
    marker_color='#5579C6',
    orientation='h'
    ))
item_fat_content_graph.update_layout(title="Item Fat Content",
                                    xaxis_title="Item_Fat_Content",
                                    yaxis_title="Count")
st.plotly_chart(item_fat_content_graph)

#plot Item_Visibility
item_visibility_graph = go.Figure( go.Histogram(
    x=train_df['Item_Visibility'],
    marker_color='#5579C6'
    ))
item_visibility_graph.update_layout(title="Item Visibility",
                                xaxis_title="Item_Visibility",
                                yaxis_title="Count")
st.plotly_chart(item_visibility_graph)

#plot Item_Visibility boxplot
item_visibility_boxplot = go.Figure( go.Box(
    x=train_df['Item_Visibility'],
    marker_color='#5579C6'
    ))
item_visibility_boxplot.update_layout(title="Item Visibility Boxplot")
st.plotly_chart(item_visibility_boxplot)

# plot Item_Type Bar chart horizontal
item_type_bar = go.Figure( go.Bar(
    y=train_df['Item_Type'].value_counts().index,
    x=train_df['Item_Type'].value_counts().values,
    marker_color='#5579C6',
    orientation='h'
    ))
item_type_bar.update_layout(title="Item Type",
                                xaxis_title="Item_Type",            
                                yaxis_title="Count")
st.plotly_chart(item_type_bar)

# plot Item_MRP Histogram
item_mrp_histogram = go.Figure( go.Histogram(
    x=train_df['Item_MRP'],
    marker_color='#5579C6'
    ))
item_mrp_histogram.update_layout(title="Item MRP Histogram",
                                xaxis_title="Item_MRP",
                                yaxis_title="Count")
st.plotly_chart(item_mrp_histogram)

# plot Item_MRP Boxplot
item_mrp_boxplot = go.Figure( go.Box(
    x=train_df['Item_MRP'],
    marker_color='#5579C6'
    ))
item_mrp_boxplot.update_layout(title="Item MRP Boxplot")
st.plotly_chart(item_mrp_boxplot)

# plot Outlet_Identifier Bar chart horizontal
outlet_identifier_bar = go.Figure( go.Bar(
    y=train_df['Outlet_Identifier'].value_counts().index,
    x=train_df['Outlet_Identifier'].value_counts().values,
    marker_color='#5579C6',
    orientation='h'
    ))
outlet_identifier_bar.update_layout(title="Outlet Identifier",
                                xaxis_title="Outlet_Identifier",
                                yaxis_title="Count")
st.plotly_chart(outlet_identifier_bar)

# plot Outlet_Establishment_Year Histogram
outlet_establishment_year_histogram = go.Figure( go.Histogram(
    x=train_df['Outlet_Establishment_Year'],
    marker_color='#5579C6'
    ))
outlet_establishment_year_histogram.update_layout(title="Outlet Establishment Year Histogram",
                                xaxis_title="Outlet_Establishment_Year",
                                yaxis_title="Count")
st.plotly_chart(outlet_establishment_year_histogram)

# plot Outlet_Size Bar chart horizontal
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

# plot Outlet_Location_Type Bar chart horizontal
outlet_location_type_bar = go.Figure( go.Bar(
    y=train_df['Outlet_Location_Type'].value_counts().index,
    x=train_df['Outlet_Location_Type'].value_counts().values,
    marker_color='#5579C6',
    orientation='h'
    ))
outlet_location_type_bar.update_layout(title="Outlet Location Type",
                                xaxis_title="Outlet_Location_Type",
                                yaxis_title="Count")
st.plotly_chart(outlet_location_type_bar)

# plot Outlet_Type Bar chart horizontal
outlet_type_bar = go.Figure( go.Bar(
    y=train_df['Outlet_Type'].value_counts().index,
    x=train_df['Outlet_Type'].value_counts().values,
    marker_color='#5579C6',
    orientation='h'
    ))
outlet_type_bar.update_layout(title="Outlet Type",
                                xaxis_title="Outlet_Type",
                                yaxis_title="Count")
st.plotly_chart(outlet_type_bar)

# plot Item_Outlet_Sales histogram
item_outlet_sales_histogram = go.Figure( go.Histogram(
    x=train_df['Item_Outlet_Sales'],
    marker_color='#5579C6'
    ))
item_outlet_sales_histogram.update_layout(title="Item Outlet Sales Histogram",
                                xaxis_title="Item_Outlet_Sales",
                                yaxis_title="Count")
st.plotly_chart(item_outlet_sales_histogram)

# plot Item_Outlet_Sales boxplot
item_outlet_sales_boxplot = go.Figure( go.Box(
    x=train_df['Item_Outlet_Sales'],
    marker_color='#5579C6'
    ))
item_outlet_sales_boxplot.update_layout(title="Item Outlet Sales Boxplot")
st.plotly_chart(item_outlet_sales_boxplot)

st.subheader("Observaciones")
st.write("""- Item_Visibility contiene outliders que deben ser tratados.""")