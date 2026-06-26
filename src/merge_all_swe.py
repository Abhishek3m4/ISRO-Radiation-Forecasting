import cdflib
import pandas as pd
import numpy as np
from pathlib import Path

DATA_ROOT = Path("data/raw/wind")
OUTPUT = Path("data/processed/swe")

OUTPUT.mkdir(parents=True, exist_ok=True)

all_data = []

for year_folder in sorted(DATA_ROOT.iterdir()):

    if not year_folder.is_dir():
        continue

    # ignore old test folder
    if year_folder.name == "wind_jan2015":
        continue

    print(f"\nScanning {year_folder.name}")

    for file in sorted(year_folder.glob("*.cdf")):

        print(f"Reading {file.name}")

        try:

            cdf = cdflib.CDF(str(file))

            epoch = cdflib.cdfepoch.to_datetime(
                cdf.varget("Epoch")
            )

            df = pd.DataFrame({

                "Epoch": epoch,

                "Np": cdf.varget("Proton_Np_nonlin"),

                "Vx": cdf.varget("Proton_VX_nonlin"),

                "Vy": cdf.varget("Proton_VY_nonlin"),

                "Vz": cdf.varget("Proton_VZ_nonlin"),

                "ThermalSpeed":
                    cdf.varget("Proton_W_nonlin"),

                "Bx": cdf.varget("BX"),

                "By": cdf.varget("BY"),

                "Bz": cdf.varget("BZ")
            })

            # NASA fill values
            df.replace(
                [
                    -1e31,
                    -999999,
                    -99999,
                    -9999,
                    -999,
                    -99,
                    99999,
                    100000,
                    999999
                ],
                np.nan,
                inplace=True
            )

            # Physical sanity checks
            df.loc[
                (df["Np"] < 0) |
                (df["Np"] > 1000),
                "Np"
            ] = np.nan

            df.loc[
                abs(df["Vx"]) > 10000,
                "Vx"
            ] = np.nan

            df.loc[
                abs(df["Vy"]) > 10000,
                "Vy"
            ] = np.nan

            df.loc[
                abs(df["Vz"]) > 10000,
                "Vz"
            ] = np.nan

            df.loc[
                (df["ThermalSpeed"] < 0) |
                (df["ThermalSpeed"] > 10000),
                "ThermalSpeed"
            ] = np.nan

            df.loc[
                abs(df["Bx"]) > 1000,
                "Bx"
            ] = np.nan

            df.loc[
                abs(df["By"]) > 1000,
                "By"
            ] = np.nan

            df.loc[
                abs(df["Bz"]) > 1000,
                "Bz"
            ] = np.nan

            all_data.append(df)

        except Exception as e:

            print(f"Skipped {file.name}")
            print(e)

swe = pd.concat(
    all_data,
    ignore_index=True
)

swe.sort_values(
    "Epoch",
    inplace=True
)

swe.drop_duplicates(
    subset="Epoch",
    inplace=True
)

# remove rows containing corrupted values
swe.dropna(
    inplace=True
)

swe.reset_index(
    drop=True,
    inplace=True
)

print("\n===================")
print("SWE MASTER DATASET")
print("===================")

print(swe.head())

print("\nRows:")
print(len(swe))

print("\nMissing Values:\n")
print(swe.isnull().sum())

print("\nStatistics:\n")
print(swe.describe())

swe.to_csv(
    OUTPUT / "wind_swe_master.csv",
    index=False
)

print("\nSaved Successfully")
print(OUTPUT / "wind_swe_master.csv")