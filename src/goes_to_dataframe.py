import cdflib
import pandas as pd
import numpy as np

cdf = cdflib.CDF(
    r"data/raw/goes/goes15_epead-science-electrons-e13ew_1min_20150101_v01.cdf"
)

epoch = cdf.varget("Epoch")

df = pd.DataFrame({
    "Epoch": epoch,
    "E1W_COR_FLUX": cdf.varget("E1W_COR_FLUX"),
    "E2W_COR_FLUX": cdf.varget("E2W_COR_FLUX"),
    "E1E_COR_FLUX": cdf.varget("E1E_COR_FLUX"),
    "E2E_COR_FLUX": cdf.varget("E2E_COR_FLUX"),
    "ORIENTATION_FLAG": cdf.varget("ORIENTATION_FLAG")
})

# Replace fill values
fill_values = [-99999, -1e31]
df.replace(fill_values, np.nan, inplace=True)

print(df.head())

print("\nMissing Values:\n")
print(df.isna().sum())

print("\nStatistics:\n")
print(df.describe())

df.to_csv(
    "data/processed/goes_20150101.csv",
    index=False
)

print("\nSaved Successfully")