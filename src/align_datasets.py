import pandas as pd

print("Loading datasets...")

goes = pd.read_csv(
    "data/processed/goes/goes_master.csv",
    parse_dates=["Epoch"]
)

swe = pd.read_csv(
    "data/processed/swe/wind_swe_master.csv",
    parse_dates=["Epoch"]
)

mfi = pd.read_csv(
    "data/processed/mfi/wind_mfi_master.csv",
    parse_dates=["Epoch"]
)

print("GOES :", len(goes))
print("SWE  :", len(swe))
print("MFI  :", len(mfi))

# ------------------------------------
# Resample all datasets to 1-minute
# ------------------------------------

print("\nResampling SWE...")

swe = (
    swe
    .set_index("Epoch")
    .resample("1min")
    .mean()
    .reset_index()
)

print("Resampling MFI...")

mfi = (
    mfi
    .set_index("Epoch")
    .resample("1min")
    .mean()
    .reset_index()
)

print("Resampling GOES...")

goes = (
    goes
    .set_index("Epoch")
    .resample("1min")
    .mean()
    .reset_index()
)

# ------------------------------------
# Apply solar wind propagation delay
# ------------------------------------

# Approximate WIND L1 → Earth delay
# Start with fixed 45 minutes

print("\nApplying 45 minute propagation delay...")

swe["Epoch"] = swe["Epoch"] + pd.Timedelta(minutes=45)
mfi["Epoch"] = mfi["Epoch"] + pd.Timedelta(minutes=45)

# ------------------------------------
# Merge SWE + MFI
# ------------------------------------

print("\nMerging SWE and MFI...")

solarwind = pd.merge(
    swe,
    mfi,
    on="Epoch",
    how="inner",
    suffixes=("_swe", "_mfi")
)

print("Solar wind rows:", len(solarwind))

# ------------------------------------
# Merge with GOES
# ------------------------------------

print("\nMerging GOES...")

master = pd.merge(
    goes,
    solarwind,
    on="Epoch",
    how="inner"
)

master.sort_values(
    "Epoch",
    inplace=True
)

master.reset_index(
    drop=True,
    inplace=True
)

print("\n====================")
print("MASTER DATASET")
print("====================")

print(master.head())

print("\nRows:")
print(len(master))

print("\nMissing Values:")
print(master.isnull().sum())

master.to_csv(
    "data/processed/final/master_dataset.csv",
    index=False
)

print("\nSaved:")
print("data/processed/final/master_dataset.csv")