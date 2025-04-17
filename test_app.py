
import pandas as pd

def test_data_load():
    df = pd.read_csv("data/electric_vehicles.csv")
    assert not df.empty, "Dataset is empty!"
    assert 'Make' in df.columns, "'Make' column missing"
