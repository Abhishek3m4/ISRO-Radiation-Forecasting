import pandas as pd

print("Loading...")

df = pd.read_csv(
    "data/processed/final/master_dataset.csv",
    parse_dates=["Epoch"]
)

print("\nBefore:")
print(df.isnull().sum())

# interpolate solar wind variables
solar_cols = [
    "Np",
    "Vx",
    "Vy",
    "Vz",
    "ThermalSpeed",
    "Bx_swe",
    "By_swe",
    "Bz_swe",
    "Bx_mfi",
    "By_mfi",
    "Bz_mfi"
]

df[solar_cols] = (
    df[solar_cols]
    .interpolate(method="linear")
    .ffill()
    .bfill()
)

# interpolate GOES
goes_cols = [
    "E1W_COR_FLUX",
    "E2W_COR_FLUX",
    "E1E_COR_FLUX",
    "E2E_COR_FLUX"
]

df[goes_cols] = (
    df[goes_cols]
    .interpolate()
    .ffill()
    .bfill()
)

# orientation flag
df["ORIENTATION_FLAG"] = (
    df["ORIENTATION_FLAG"]
    .ffill()
    .bfill()
)

print("\nAfter:")
print(df.isnull().sum())

df.to_csv(
    "data/processed/final/master_dataset_clean.csv",
    index=False
)

print("\nSaved:")
print("data/processed/final/master_dataset_clean.csv")