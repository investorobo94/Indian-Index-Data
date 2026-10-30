python
# script_a.py
import pandas as pd

# Option A: Direct variable definition
my_dataset = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 92, 78]
})

# Option B (Recommended if loading from a file): Function wrapper
def load_my_dataset():
    # Replace with your actual path or database query
    return pd.read_csv("data.csv") 
