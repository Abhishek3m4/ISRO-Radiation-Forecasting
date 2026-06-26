import cdflib
import pandas as pd
import numpy as np
from pathlib import Path

# ==========================
# GOES DATA ROOT
# ==========================

DATA_ROOT = Path("data/raw/goes")

all_data = []

# Loop through all year folders
for year_folder in sorted(DATA_ROOT.iterdir()):

    if not year_folder.is_dir():
        continue

    # Ignore old testing folder
    if year_folder.name == "goes_jan2015":
        continue

    print(f"\nScanning {year_folder.name}")

    for file in sorted(year_folder.glob("*.cdf")):

        print(f"Reading {file.name}")

        cdf = cdflib.CDF(str(file))

        epoch = cdflib.cdfepoch.to_datetime(
            cdf.varget("Epoch")
        )

        df = pd.DataFrame({

            "Epoch": epoch,

            "E1W_COR_FLUX":
                cdf.varget("E1W_COR_FLUX"),

            "E2W_COR_FLUX":
                cdf.varget("E2W_COR_FLUX"),

            "E1E_COR_FLUX":
                cdf.varget("E1E_COR_FLUX"),

            "E2E_COR_FLUX":
                cdf.varget("E2E_COR_FLUX"),

            "ORIENTATION_FLAG":
                cdf.varget("ORIENTATION_FLAG")

        })

        # NASA fill values
        
        df.replace(
    [-99999, -1e31, -99],
    np.nan,
    inplace=True
)

        all_data.append(df)

# ==========================
# Merge Everything
# ==========================

goes_df = pd.concat(
    all_data,
    ignore_index=True
)

goes_df.sort_values(
    "Epoch",
    inplace=True
)

goes_df.drop_duplicates(
    subset="Epoch",
    inplace=True
)

goes_df.reset_index(
    drop=True,
    inplace=True
)

print("\n==========================")
print("GOES MASTER DATASET")
print("==========================")

print(goes_df.head())

print("\nRows:")
print(len(goes_df))

print("\nMissing Values:\n")
print(goes_df.isnull().sum())

print("\nStatistics:\n")
print(goes_df.describe())

# ==========================
# Save
# ==========================

OUTPUT = Path(
    "data/processed/goes"
)

OUTPUT.mkdir(
    parents=True,
    exist_ok=True
)

goes_df.to_csv(

    OUTPUT /
    "goes_master.csv",

    index=False

)

print("\nSaved Successfully")

print(
    OUTPUT /
    "goes_master.csv"
)