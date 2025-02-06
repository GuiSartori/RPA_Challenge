# utils/data_utils.py
import pandas as pd

def load_excel(file_path):
    """Carrega dados de um arquivo Excel."""
    return pd.read_excel(file_path)
