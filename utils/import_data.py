import pandas as pd

def import_train_data():
    train_df = pd.read_csv('data/Train_BigMart.csv')
    return train_df

def import_test_data():
    test_df = pd.read_csv('data/Test_BigMart.csv')
    return test_df

