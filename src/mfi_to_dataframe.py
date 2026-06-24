# src/mfi_to_dataframe.py

import cdflib
import pandas as pd
import numpy as np

cdf = cdflib.CDF(
    r"data/raw/wind_mfi/wi_h0_mfi_20260601_v03.cdf"
)

epoch = cdf.varget("Epoch")
epoch = cdflib.cdfepoch.to_datetime(
    cdf.varget("Epoch")
)
bgsm = cdf.varget("BGSM")

df = pd.DataFrame({
    "Epoch": epoch,
    "Bx": bgsm[:,0],
    "By": bgsm[:,1],
    "Bz": bgsm[:,2]
})

print(df.head())

print("\nMissing Values:\n")
print(df.isnull().sum())

df.to_csv(
    "data/processed/wind_mfi_20260601.csv",
    index=False
)

print("\nSaved Successfully")