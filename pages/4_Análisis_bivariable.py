import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go

st.title('Análisis bivariable')
st.markdown('Se analiza el comportamiento de las variables respecto a la variable objetivo.')

train_df = st.session_state["train_df"]

# Item_Outlet_Sales vs Item_Weight scatter plot
item_outlet_sales_item_weight_scatter = go.Figure( go.Scatter(
    x=train_df['Item_Weight'],
    y=train_df['Item_Outlet_Sales'],
    mode='markers',
    marker_color='#5579C6'
    ))
item_outlet_sales_item_weight_scatter.update_layout(title="Item Outlet Sales vs Item Weight Scatter Plot",
                                xaxis_title="Item_Weight",
                                yaxis_title="Item_Outlet_Sales")
st.plotly_chart(item_outlet_sales_item_weight_scatter)

#plot tem_Outlet_Sales main by Item_Fat_Content
item_fat_content_main_by_item_outlet_sales = train_df.groupby(['Item_Fat_Content']).mean()["Item_Outlet_Sales"]
# plot bar chart
item_fat_content_main_by_item_outlet_sales_bar = go.Figure( go.Bar(
    y=item_fat_content_main_by_item_outlet_sales.index,
    x=item_fat_content_main_by_item_outlet_sales.values,
    marker_color='#5579C6',
    orientation='h'
    ))
item_fat_content_main_by_item_outlet_sales_bar.update_layout(title="Item Outlet Sales Main by Item Fat Content",
                                xaxis_title="Item_Outlet_Sales",
                                yaxis_title="Item_Fat_Content")
st.plotly_chart(item_fat_content_main_by_item_outlet_sales_bar)

# Item_Visibility vs Item_Outlet_Sales scatter plot
item_visibility_item_outlet_sales_scatter = go.Figure( go.Scatter(
    x=train_df['Item_Visibility'],
    y=train_df['Item_Outlet_Sales'],
    mode='markers',
    marker_color='#5579C6'
    ))
item_visibility_item_outlet_sales_scatter.update_layout(title="Item Visibility vs Item Outlet Sales Scatter Plot",
                                xaxis_title="Item_Visibility",
                                yaxis_title="Item_Outlet_Sales")
st.plotly_chart(item_visibility_item_outlet_sales_scatter)

# Item_Outlet_Sales mean by Item_Type 
item_outlet_sales_item_type_media = train_df.groupby(['Item_Type']).mean()["Item_Outlet_Sales"]
# plot bar chart
item_outlet_sales_item_type_media_bar = go.Figure( go.Bar(
    y=item_outlet_sales_item_type_media.index,
    x=item_outlet_sales_item_type_media.values,
    marker_color='#5579C6',
    orientation='h'
    ))
item_outlet_sales_item_type_media_bar.update_layout(title="Item Outlet Sales Mean by Item Type ",
                                xaxis_title="Item_Outlet_Sales",    
                                yaxis_title="Item_Type")
st.plotly_chart(item_outlet_sales_item_type_media_bar)

# Item_MRP vs Item_Outlet_Sales scatter plot
item_mrp_item_outlet_sales_scatter = go.Figure( go.Scatter(
    x=train_df['Item_MRP'],
    y=train_df['Item_Outlet_Sales'],
    mode='markers',
    marker_color='#5579C6'
    ))
item_mrp_item_outlet_sales_scatter.update_layout(title="Item MRP vs Item Outlet Sales Scatter Plot",
                                xaxis_title="Item_MRP",
                                yaxis_title="Item_Outlet_Sales")
st.plotly_chart(item_mrp_item_outlet_sales_scatter)

# Item_Outlet_Sales mean by Outler identifier
item_outlet_sales_mean_by_outlet_identifier = train_df.groupby(['Outlet_Identifier']).mean()["Item_Outlet_Sales"]
# plot bar chart
item_outlet_sales_mean_by_outlet_identifier_bar = go.Figure( go.Bar(
    y=item_outlet_sales_mean_by_outlet_identifier.index, 
    x=item_outlet_sales_mean_by_outlet_identifier.values,
    marker_color='#5579C6',
    orientation='h'
    ))
item_outlet_sales_mean_by_outlet_identifier_bar.update_layout(title="Item Outlet Sales Mean by Outlet Identifier",
                                xaxis_title="Item_Outlet_Sales",
                                yaxis_title="Outlet_Identifier")
st.plotly_chart(item_outlet_sales_mean_by_outlet_identifier_bar)

# Item_Outlet_Sales mean by Outlet_Establishment_Year
item_outlet_sales_mean_by_outlet_establishment_year = train_df.groupby(['Outlet_Establishment_Year']).mean()["Item_Outlet_Sales"]
# plot bar chart
item_outlet_sales_mean_by_outlet_establishment_year_bar = go.Figure( go.Bar(
    y=item_outlet_sales_mean_by_outlet_establishment_year.index,
    x=item_outlet_sales_mean_by_outlet_establishment_year.values,
    marker_color='#5579C6',
    orientation='h'
    ))
item_outlet_sales_mean_by_outlet_establishment_year_bar.update_layout(title="Item Outlet Sales Mean by Outlet Establishment Year",
                                xaxis_title="Item_Outlet_Sales",
                                yaxis_title="Outlet_Establishment_Year")
st.plotly_chart(item_outlet_sales_mean_by_outlet_establishment_year_bar)

# Item_Outlet_Sales mean by Outlet_Size
item_outlet_sales_mean_by_outlet_size = train_df.groupby(['Outlet_Size']).mean()["Item_Outlet_Sales"]
# plot bar chart
item_outlet_sales_mean_by_outlet_size_bar = go.Figure( go.Bar(
    y=item_outlet_sales_mean_by_outlet_size.index,
    x=item_outlet_sales_mean_by_outlet_size.values,
    marker_color='#5579C6',
    orientation='h'
    ))
item_outlet_sales_mean_by_outlet_size_bar.update_layout(title="Item Outlet Sales Mean by Outlet Size",
                                xaxis_title="Item_Outlet_Sales",
                                yaxis_title="Outlet_Size")
st.plotly_chart(item_outlet_sales_mean_by_outlet_size_bar)

# Item_Outlet_Sales mean by Outlet_Location_Type
item_outlet_sales_mean_by_outlet_location_type = train_df.groupby(['Outlet_Location_Type']).mean()["Item_Outlet_Sales"]
# plot bar chart
item_outlet_sales_mean_by_outlet_location_type_bar = go.Figure( go.Bar(
    y=item_outlet_sales_mean_by_outlet_location_type.index,
    x=item_outlet_sales_mean_by_outlet_location_type.values,
    marker_color='#5579C6',
    orientation='h'
    ))
item_outlet_sales_mean_by_outlet_location_type_bar.update_layout(title="Item Outlet Sales Mean by Outlet Location Type",
                                xaxis_title="Item_Outlet_Sales",
                                yaxis_title="Outlet_Location_Type")
st.plotly_chart(item_outlet_sales_mean_by_outlet_location_type_bar)

# Item_Outlet_Sales mean by Outlet_Type
item_outlet_sales_mean_by_outlet_type = train_df.groupby(['Outlet_Type']).mean()["Item_Outlet_Sales"]
# plot bar chart
item_outlet_sales_mean_by_outlet_type_bar = go.Figure( go.Bar(
    y=item_outlet_sales_mean_by_outlet_type.index,
    x=item_outlet_sales_mean_by_outlet_type.values,
    marker_color='#5579C6',
    orientation='h'
    ))
item_outlet_sales_mean_by_outlet_type_bar.update_layout(title="Item Outlet Sales Mean by Outlet Type",
                                xaxis_title="Item_Outlet_Sales",
                                yaxis_title="Outlet_Type")
st.plotly_chart(item_outlet_sales_mean_by_outlet_type_bar)
