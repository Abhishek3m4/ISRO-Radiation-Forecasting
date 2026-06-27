# ISRO Radiation Environment Forecasting

Forecasting energetic electron fluxes for ISRO geostationary satellites using:

- GOES-15 Electron Flux
- WIND SWE H1 Solar Wind Plasma
- WIND MFI Magnetic Field

## Dataset Period

2010–2020

## Pipeline

1. NASA CDAWeb data download
2. CDF parsing
3. Data cleaning
4. Missing value handling
5. Time alignment
6. Solar wind propagation delay correction
7. Feature engineering
8. Machine learning forecasting

## Technologies

- Python
- Pandas
- NumPy
- cdflib
- scikit-learn
- PyTorch
- Git
- aria2

## Current Status

✓ Dataset acquisition  
✓ Preprocessing  
✓ Feature engineering  

Next:
- Random Forest
- XGBoost
- LSTM forecasting