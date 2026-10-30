# script_b.py
# Import the specific variable or function from script_a
from script_a import my_dataset, load_my_dataset

# If you used Option A (Direct variable):
print("Using direct variable:")
print(my_dataset.head())

# If you used Option B (Function wrapper):
print("\nUsing function wrapper:")
df = load_my_dataset()
print(df.describe())
