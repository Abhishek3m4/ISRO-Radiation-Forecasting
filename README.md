<div align="center">

# 🛰️ GaganiX

### AI-Driven Space Weather Radiation Forecasting System

**Multi-horizon energetic electron-flux forecasting for geostationary satellite environments**

<br>

<img src="assets/dashboard.jpeg" alt="GaganiX Dashboard" width="900">

<br><br>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-ML%20Forecasting-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)](#)
[![Hackathon](https://img.shields.io/badge/Bhartiya%20Antariksh%20Hackathon-2026-0A66C2?style=for-the-badge)](#)

</div>

---

## 🌌 Overview

**GaganiX** is an AI-driven space-weather forecasting system developed for energetic particle radiation forecasting near geostationary orbit.

It processes **11 years of satellite radiation and solar-wind data** and generates **30-min, 45-min, 6-hr and 12-hr** electron-flux forecasts through an interactive dashboard.

---

## ✨ Key Features

- 🛰️ **Satellite Radiation Analysis** — Processes energetic electron and proton observations from satellite datasets.
- ☀️ **Solar-Wind Analysis** — Incorporates solar-wind and interplanetary magnetic-field parameters.
- 🤖 **AI-Based Forecasting** — Machine-learning and deep-learning pipeline for energetic electron-flux prediction.
- ⏱️ **Multi-Horizon Forecasting** — Supports 30-minute, 45-minute, 6-hour and 12-hour prediction horizons.
- 📊 **Interactive Dashboard** — Streamlit interface for monitoring data, forecasts and radiation-related indicators.
- 🔬 **Scientific Data Pipeline** — CDF data reading, preprocessing, feature engineering, model training and validation.

---

# 📸 Project Dashboard

The system provides an interactive interface for examining radiation conditions and forecasting outputs.

<div align="center">

<img src="assets/dashboard.jpeg" alt="GaganiX Interactive Dashboard" width="900">

<br>

<sub><b>GaganiX — Interactive Space Weather Forecasting Dashboard</b></sub>

</div>

---

# 📈 Forecasting

The forecasting module provides multi-horizon predictions for energetic electron flux.

<div align="center">

<img src="assets/forecast.jpeg" alt="GaganiX Forecast" width="850">

<br>

<sub><b>Multi-horizon electron-flux forecasting output</b></sub>

</div>

---

# 📊 Data & Radiation Analysis

<div align="center">

<table>
<tr>

<td align="center">
<img src="assets/data_visualization.jpeg" width="420">
<br>
<b>Satellite / Solar-Wind Data Visualization</b>
</td>

<td align="center">
<img src="assets/GOES_Electron_flux.jpeg" width="420">
<br>
<b>GOES Electron Flux Analysis</b>
</td>

</tr>
</table>

</div>

---

# ⚠️ Radiation Risk Analysis

<div align="center">

<img src="assets/risk_score.jpeg" alt="GaganiX Radiation Risk Score" width="700">

<br>

<sub><b>Radiation risk assessment and forecasting indicator</b></sub>

</div>

---

# 🔬 Additional Scientific Data

<div align="center">

<table>
<tr>

<td align="center">
<img src="assets/IMF_data.jpeg" width="400">
<br>
<b>Interplanetary Magnetic Field Data</b>
</td>

<td align="center">
<img src="assets/GOES_proton_data.jpeg" width="400">
<br>
<b>GOES Proton Data</b>
</td>

</tr>
</table>

</div>

---

# 🧠 System Architecture

```mermaid
flowchart LR

    A[GOES Satellite Data]
    B[WIND Solar-Wind Data]

    A --> C[CDF Data Reader]
    B --> C

    C --> D[Data Preprocessing]

    D --> E[Data Cleaning]
    E --> F[Feature Engineering]

    F --> G[ML / Deep Learning Models]

    G --> H[30-Min Forecast]
    G --> I[45-Min Forecast]
    G --> J[6-Hour Forecast]
    G --> K[12-Hour Forecast]

    H --> L[Forecast Analysis]
    I --> L
    J --> L
    K --> L

    L --> M[Radiation Risk Analysis]

    M --> N[Streamlit Dashboard]

    N --> O[Engineering Visualization]
