import cdflib
import pandas as pd
import numpy as np

cdf = cdflib.CDF(
    r"data/raw/goes/goes_jan2015/goes15_epead-science-electrons-e13ew_1min_20150101_v01.cdf"
)

epoch = cdflib.cdfepoch.to_datetime(
    cdf.varget("Epoch")
)

df = pd.DataFrame({
    "Epoch": epoch,
    "E1W_COR_FLUX": cdf.varget("E1W_COR_FLUX"),
    "E2W_COR_FLUX": cdf.varget("E2W_COR_FLUX"),
    "E1E_COR_FLUX": cdf.varget("E1E_COR_FLUX"),
    "E2E_COR_FLUX": cdf.varget("E2E_COR_FLUX"),
    "ORIENTATION_FLAG": cdf.varget("ORIENTATION_FLAG")
})

df.replace(-1e31, np.nan, inplace=True)

print(df.head())

print("\nRows:", len(df))

print("\nMissing Values:\n")
print(df.isnull().sum())

df.to_csv(
    "data/processed/goes_2015_01.csv",
    index=False
)

print("\nSaved Successfully")