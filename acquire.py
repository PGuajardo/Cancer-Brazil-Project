import pandas as pd
import os

def get_brazil_data():
    filename = "cancer_data_eng.csv"

    if os.path.isfile(filename):
        brazil_cancer = pd.read_csv(filename)
    else:
        print('No file .csv file exists')

    return brazil_cancer