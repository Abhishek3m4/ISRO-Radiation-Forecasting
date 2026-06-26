import cdflib
import pandas as pd
import numpy as np

file_path = r"data/raw/wind_mfi/wind_mfi_jan2015/wi_h0_mfi_20150101_v05.cdf"

cdf = cdflib.CDF(file_path)

epoch = cdflib.cdfepoch.to_datetime(
    cdf.varget("Epoch")
)

bgsm = cdf.varget("BGSM")

df = pd.DataFrame({
    "Epoch": epoch,
    "Bx": bgsm[:, 0],
    "By": bgsm[:, 1],
    "Bz": bgsm[:, 2]
})

# Replace possible fill values
df.replace(-1e31, np.nan, inplace=True)

print(df.head())

print("\nMissing Values:\n")
print(df.isnull().sum())

print("\nStatistics:\n")
print(df.describe())

df.to_csv(
    "data/processed/wind_mfi_20150101.csv",
    index=False
)

print("\nSaved Successfully")