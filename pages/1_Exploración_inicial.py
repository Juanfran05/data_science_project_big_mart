import pandas as pd
import numpy as np
import streamlit as st

from utils.import_data import import_train_data
from utils.explore_data import profile_data

st.title("Explore the data 📊")


train_df = import_train_data()



profile_data(train_df)

st.header("Observations")
st.markdown("The Item fat content need a fix on categorical variables.")
st.markdown("Reshaping on outler identifier maybe a good idea.")