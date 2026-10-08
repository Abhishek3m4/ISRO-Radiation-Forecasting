<div align="center">

<a href="https://github.com/Abhishek3m4/ISRO-Radiation-Forecasting">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,100:203a43&height=180&section=header&text=GaganiX&fontSize=55&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=AI-Driven%20Space%20Weather%20Radiation%20Forecasting%20System&descAlignY=62&descSize=18" width="100%" />
</a>

### 🛰️ Multi-Horizon Energetic Particle Radiation Forecasting for Geostationary Satellites

<p>
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Bhartiya%20Antariksh%20Hackathon-2026-0A66C2?style=for-the-badge" alt="Hackathon">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PyTorch-ML%20Forecasting-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
</p>

</div>

---

# 🌌 Overview

**GaganiX** is an AI-driven space-weather forecasting system developed for energetic particle radiation forecasting near geostationary orbit.

The system processes **11 years of satellite radiation and solar-wind datasets** and generates **30-min, 45-min, 6-hr and 12-hr** forecasts through an interactive engineering dashboard.

---

# ✨ Key Features

- 🛰️ **Satellite Radiation Analysis** — Processes energetic particle observations from satellite datasets.
- ☀️ **Solar-Wind Analysis** — Uses solar-wind and interplanetary magnetic-field parameters.
- 🤖 **AI-Based Forecasting** — Machine-learning/deep-learning pipeline for energetic electron-flux prediction.
- ⏱️ **Multi-Horizon Forecasting** — Supports 30-minute, 45-minute, 6-hour and 12-hour horizons.
- 📊 **Interactive Dashboard** — Streamlit-based interface for data, forecast and risk visualization.
- 🔬 **Scientific Data Pipeline** — CDF reading, preprocessing, feature engineering, training and validation.

---

# 📸 Project Dashboard

<div align="center">

<img src="assets/dashboard.jpeg" alt="GaganiX Dashboard" width="900">

<br>

<sub><b>GaganiX — Interactive Space Weather Forecasting Dashboard</b></sub>

</div>

---

# 📈 Forecasting

The forecasting module provides multi-horizon energetic electron-flux prediction for short-term and extended forecasting requirements.

<div align="center">

<img src="assets/forecast.jpeg" alt="GaganiX Forecast" width="850">

<br>

<sub><b>Multi-horizon forecast visualization</b></sub>

</div>

---

# 📊 Data Analysis

<div align="center">

<table>
<tr>

<td align="center">
<img src="assets/data_visualization.jpeg" width="420">
<br>
<b>Satellite & Solar-Wind Data Visualization</b>
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

<img src="assets/risk_score.jpeg" alt="Radiation Risk Score" width="700">

<br>

<sub><b>Radiation risk assessment and visualization</b></sub>

</div>

---

# 🛰️ Additional Space-Weather Data

<div align="center">

<table>
<tr>

<td align="center">
<img src="assets/IMF_data.jpeg" width="420">
<br>
<b>Interplanetary Magnetic Field Data</b>
</td>

<td align="center">
<img src="assets/GOES_proton_data.jpeg" width="420">
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

    M --> N[Interactive Dashboard]

    N --> O[Engineering Visualization]
