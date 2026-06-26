import cdflib
import pandas as pd
import numpy as np
from pathlib import Path

DATA_ROOT = Path("data/raw/wind_mfi")
OUTPUT = Path("data/processed/mfi")

OUTPUT.mkdir(parents=True, exist_ok=True)

all_data = []

for year_folder in sorted(DATA_ROOT.iterdir()):

    if not year_folder.is_dir():
        continue

    # Ignore old testing folder
    if year_folder.name == "wind_mfi_jan2015":
        continue

    print(f"\nScanning {year_folder.name}")

    for file in sorted(year_folder.glob("*.cdf")):

        print(f"Reading {file.name}")

        try:

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

            df.replace(
                [-1e31, -99999, -99],
                np.nan,
                inplace=True
            )

            all_data.append(df)

        except Exception as e:

            print(f"Skipped {file.name}")
            print(e)

mfi = pd.concat(
    all_data,
    ignore_index=True
)

mfi.sort_values(
    "Epoch",
    inplace=True
)

mfi.drop_duplicates(
    subset="Epoch",
    inplace=True
)

mfi.reset_index(
    drop=True,
    inplace=True
)

print("\n===================")
print("MFI MASTER DATASET")
print("===================")

print(mfi.head())

print("\nRows:")
print(len(mfi))

print("\nMissing Values:\n")
print(mfi.isnull().sum())

print("\nStatistics:\n")
print(mfi.describe())

mfi.to_csv(
    OUTPUT / "wind_mfi_master.csv",
    index=False
)

print("\nSaved Successfully")
print(OUTPUT / "wind_mfi_master.csv")