import pandas as pd

# Load files
wind = pd.read_csv("data/processed/wind_20260601.csv")
mfi = pd.read_csv("data/processed/wind_mfi_20260601.csv")
goes = pd.read_csv("data/processed/goes_20150101.csv")

print("\n===== WIND SWE =====")
print(wind["Epoch"].head())
print("dtype:", wind["Epoch"].dtype)

print("\n===== WIND MFI =====")
print(mfi["Epoch"].head())
print("dtype:", mfi["Epoch"].dtype)

print("\n===== GOES =====")
print(goes["Epoch"].head())
print("dtype:", goes["Epoch"].dtype)