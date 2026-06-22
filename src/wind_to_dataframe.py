import cdflib
import pandas as pd
import numpy as np

file_path = r"data/raw/wind/wi_k0_swe_20260601_v01.cdf"

cdf = cdflib.CDF(file_path)

epoch = cdf.varget("Epoch")
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

df.to_csv("data/processed/wind_20260601.csv", index=False)

print(df.head())
print("\nSaved Successfully")