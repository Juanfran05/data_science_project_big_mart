import streamlit as st
import pandas as pd


import datetime as dt
from sklearn.preprocessing import LabelEncoder

from utils.import_data import import_test_data


st.title('Aplicación del modelo')
st.markdown('Se realizó el procesamiento respectivo al dataset test y se aplicó \
    el modelo entrenado para obtener la predicción')

test_df = import_test_data()
# Item_Weight fillna with median
test_df['Item_Weight'].fillna(test_df['Item_Weight'].median(), inplace=True)
test_df.replace({"Item_Fat_Content": {"low fat": "Low Fat", "Low Fat": "Low Fat", "reg": "Regular", "Regular": "Regular", "reg ": "Regular", "LF": "Low Fat"}} , inplace=True)
item_visibility_avg = test_df.groupby("Item_Identifier").mean()["Item_Visibility"] 
test_df['Item_Visibility'] = test_df.apply(lambda x: item_visibility_avg[x["Item_Identifier"]] if x["Item_Visibility"] ==0 else x["Item_Visibility"], axis=1)
outlet_size_mode = test_df.pivot_table(values='Outlet_Size',
      columns='Outlet_Type',aggfunc=lambda x:x.mode())
test_df["Outlet_Size"].fillna("None", inplace=True)
test_df["Outlet_Size"] = test_df.apply(lambda x: outlet_size_mode.loc['Outlet_Size'][x["Outlet_Type"]] if x["Outlet_Size"] == "None" else x["Outlet_Size"], axis=1)
test_df["Item_Type_Id"] = test_df["Item_Identifier"].apply(lambda x: x[0:2])
current_year =  dt.datetime.now().year
test_df["Outlet_Age"] = current_year - test_df["Outlet_Establishment_Year"] 
label = LabelEncoder()
vars_label_encoder = ['Item_Fat_Content', 'Outlet_Identifier',
        'Outlet_Size', 'Outlet_Location_Type',
       'Outlet_Type', 'Item_Type_Id'] 
for col in vars_label_encoder:
    test_df[col] = label.fit_transform(test_df[col])
vars_dummy = ['Item_Fat_Content', 'Outlet_Identifier',
        'Outlet_Size', 'Outlet_Location_Type',
       'Outlet_Type', 'Item_Type_Id'] 
test_df = pd.get_dummies(test_df, columns=vars_dummy)

regression = st.session_state["regression_model"]
cols_for_model = st.session_state["cols_for_model"]
X_test = test_df[cols_for_model]
prediction = regression.predict(X_test)
result = X_test.copy()
result["prediction_sales"] = prediction
st.table(result.head(10))