# utils/data_utils.py
import pandas as pd

def load_excel(file_path):
    
    # Loads data from an Excel file
    return pd.read_excel(file_path)
