import yfinance as yf
import os

# Define the list of assets (tickers)
tickers = [
    "EURUSD=X", "JPY=X", "GBPUSD=X", "GC=F", "SI=F",
    "BTC-USD", "ETH-USD", "LINK-USD", "AVAX-USD", "CL=F"
]

# Define the output folder for raw data
output_folder = "data/raw"

# Create the folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through each ticker and fetch data
for ticker in tickers:
    print(f"Fetching data for {ticker}...")
    try:
        # Download 10 years of daily data
        data = yf.download(ticker, period="10y", interval="1d")

        # Save the data to CSV if data is not empty
        if not data.empty:
            # Replace any special characters in the filename
            filename = ticker.replace("=", "-").replace("/", "-") + ".csv"
            filepath = os.path.join(output_folder, filename)
            data.to_csv(filepath)
            print(f"Saved {ticker} to {filepath}")
        else:
            print(f"No data available for {ticker}.")

    except Exception as e:
        # Print any errors during download
        print(f"Error fetching {ticker}: {e}")
