import cdflib
import pandas as pd
import numpy as np
from pathlib import Path

DATA_ROOT = Path("data/raw/swe")
OUTPUT = Path("data/processed/swe")

OUTPUT.mkdir(parents=True, exist_ok=True)

all_data = []

for year_folder in sorted(DATA_ROOT.iterdir()):

    if not year_folder.is_dir():
        continue

    print(f"\nScanning {year_folder.name}")

    for file in sorted(year_folder.glob("*.cdf")):

        print(f"Reading {file.name}")

        cdf = cdflib.CDF(str(file))

        epoch = cdflib.cdfepoch.to_datetime(
            cdf.varget("Epoch")
        )

        velocity = cdf.varget("V_GSE")

        df = pd.DataFrame({

            "Epoch": epoch,

            "Density":
                cdf.varget("Np"),

            "ThermalSpeed":
                cdf.varget("THERMAL_SPD"),

            "Vx":
                velocity[:,0],

            "Vy":
                velocity[:,1],

            "Vz":
                velocity[:,2]

        })

        df.replace(
            [-1e31, -99999],
            np.nan,
            inplace=True
        )

        all_data.append(df)

monthly = pd.concat(
    all_data,
    ignore_index=True
)

monthly.sort_values(
    "Epoch",
    inplace=True
)

monthly.drop_duplicates(
    subset="Epoch",
    inplace=True
)

monthly.reset_index(
    drop=True,
    inplace=True
)

print("\nRows:", len(monthly))

print("\nMissing Values:\n")

print(
    monthly.isnull().sum()
)

monthly.to_csv(
    OUTPUT /
    "wind_swe_master.csv",
    index=False
)

print("\nSaved Successfully")