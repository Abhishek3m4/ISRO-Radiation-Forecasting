import pandas as pd

print("Loading master dataset...")

df = pd.read_csv(
    "data/processed/final/master_dataset_clean.csv",
    parse_dates=["Epoch"]
)

features = [
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

# 30 min lag
for col in features:
    df[f"{col}_30m"] = df[col].shift(30)

# 45 min lag
for col in features:
    df[f"{col}_45m"] = df[col].shift(45)

# 6 hour lag
for col in features:
    df[f"{col}_6h"] = df[col].shift(360)

# 12 hour lag
for col in features:
    df[f"{col}_12h"] = df[col].shift(720)

# target variable
df["target_30m"] = df["E1W_COR_FLUX"].shift(-30)
df["target_6h"] = df["E1W_COR_FLUX"].shift(-360)
df["target_12h"] = df["E1W_COR_FLUX"].shift(-720)

df.dropna(inplace=True)

print("\nRows after feature engineering:")
print(len(df))

print("\nColumns:")
print(len(df.columns))

df.to_csv(
    "data/processed/final/features_dataset.csv",
    index=False
)

print("\nSaved:")
print("data/processed/final/features_dataset.csv")