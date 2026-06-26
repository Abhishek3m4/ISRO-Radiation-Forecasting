import cdflib
import pandas as pd
import numpy as np
from pathlib import Path

DATA_FOLDER = Path(
    "data/raw/wind_mfi/wind_mfi_jan2015"
)

all_data = []

files = sorted(
    DATA_FOLDER.glob("wi_h0_mfi_*.cdf")
)

print(f"Found {len(files)} MFI files\n")

for file in files:

    print(f"Reading {file.name}")

    cdf = cdflib.CDF(str(file))

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

    df.replace(-1e31, np.nan, inplace=True)

    all_data.append(df)

monthly_df = pd.concat(
    all_data,
    ignore_index=True
)

monthly_df.drop_duplicates(
    subset=["Epoch"],
    inplace=True
)

monthly_df.sort_values(
    by="Epoch",
    inplace=True
)

monthly_df.reset_index(
    drop=True,
    inplace=True
)

print("\nRows:", len(monthly_df))
print("\nMissing Values:\n")
print(monthly_df.isnull().sum())

monthly_df.to_csv(
    "data/processed/wind_mfi_2015_01.csv",
    index=False
)

print("\nSaved Successfully")