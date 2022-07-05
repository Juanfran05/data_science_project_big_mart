import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

def profile_data(df):    
    pr = df.profile_report()
    return st_profile_report(pr)