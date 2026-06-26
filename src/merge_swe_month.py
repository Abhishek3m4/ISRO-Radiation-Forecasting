import cdflib
import pandas as pd
import numpy as np
from pathlib import Path

DATA_FOLDER = Path(
    "data/raw/wind/wind_jan2015"
)

all_data = []

files = sorted(
    DATA_FOLDER.glob("wi_k0_swe_*.cdf")
)

print(f"Found {len(files)} SWE files\n")

for file in files:

    print(f"Reading {file.name}")

    cdf = cdflib.CDF(str(file))

    epoch = cdflib.cdfepoch.to_datetime(
        cdf.varget("Epoch")
    )

    density = cdf.varget("Np")
    thermal_speed = cdf.varget("THERMAL_SPD")
    velocity = cdf.varget("V_GSE")

    df = pd.DataFrame({
        "Epoch": epoch,
        "Density": density,
        "ThermalSpeed": thermal_speed,
        "Vx": velocity[:,0],
        "Vy": velocity[:,1],
        "Vz": velocity[:,2]
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
    "data/processed/wind_swe_2015_01.csv",
    index=False
)

print("\nSaved Successfully")