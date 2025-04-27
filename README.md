# FX Portfolio Tracker
Track FX, Commodities and Crypto Assets with Real-Time Data
# FX & Commodities Real-Time Dashboard

## Overview
A real-time financial analytics dashboard fetching live data for major FX pairs, Commodities, and Crypto assets using Yahoo Finance (Later Bloomberg).  
Designed for professional trading, portfolio tracking, risk management, and decision-making support.

Assets tracked:
- FX: EUR/USD, GBP/USD, JPY/USD
- Commodities: XAU/USD (Gold), XAG/USD (Silver), OIL/USD (WTI Crude Oil)
- Crypto: BTC/USDT, ETH/USDT, LINK/USDT, AVAX/USDT

---

## Project Goals
- Fetch and store real-time and historical price data automatically.
- Clean, transform, and structure the data for analytics.
- Calculate key trading metrics (e.g. rolling P&L, VaR, Sharpe ratio).
- Build interactive dashboards and monitoring tools.
- Provide easy-to-read analytics for trading decisions.

---

## Project Structure
- /data/ : Scripts and storage for historical market data.
- /analysis/ : Rolling P&L, VaR calculations, and portfolio metrics
- /dashboards/ : BI dashboards (Power BI or Streamlit App)
- /notebooks/ : Exploratory data analysis (EDA) and modeling
- /reports/ : Generated performance reports
- /README.md : Project description, setup instructions, and usage guide

---

## Tech Stack
- **Python** (main programming language)
- **yfinance** (for real-time and historical financial data)
- **Pandas** (for data manipulation)
- **Matplotlib / Plotly** (for visualization)
- **Dash** or **Streamlit** (for building dashboards)
- **SQL** or **SQLite** (for storing clean historical data)
- **GitHub Actions** (for automating daily data pulls)

---

## How It Works

1. **Connect to Yahoo Finance (later to Bloomberg)**
   - Fetch real-time prices for selected assets.
   
2. **Data Cleaning & Storage**
   - Remove outliers, fill missing data, structure into clean time series.

3. **Analytics & Metrics Calculation**
   - Calculate Rolling P&L, Volatility, Sharpe Ratios, VaR and more.

4. **Dashboard Development**
   - Build an interactive dashboard to display KPIs, graphs, alerts, and historical performance.

---

## Setup Instructions

1. Clone this repository
2. Install Python dependencies (pip install -r requirements.txt)
3. Run data fetching scripts inside /data/.
4. Start analyzing and visualizing!

## Future Extensions
- Connection to Bloomberg API
- Machine Learning-based trading signals
- Automated alert system for significant risk changes

git clone https://github.com/nikolaspsarris/fx-dashboard.git
