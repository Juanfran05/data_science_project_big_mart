import streamlit as st

from utils.import_data import import_train_data
from utils.import_data import import_test_data

st.title("Vista Previa 📊")

train_data = import_train_data()
test_data = import_test_data()

st.subheader("Train data")
st.dataframe(data=train_data.head(10))

st.subheader("Test data")
st.dataframe(data=test_data.head(10))
