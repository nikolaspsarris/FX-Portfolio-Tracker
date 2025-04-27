# Import necessary libraries
import os
import pandas as pd

# Define folders
raw_data_folder = "./raw/"
cleaned_data_folder = "./cleaned/"
bad_data_folder = "./bad_data/"

# Make sure output folders exist
os.makedirs(cleaned_data_folder, exist_ok=True)
os.makedirs(bad_data_folder, exist_ok=True)

# List all raw CSV files
files = os.listdir(raw_data_folder)

for file in files:
    if file.endswith('.csv'):
        # Read the raw CSV
        df = pd.read_csv(os.path.join(raw_data_folder, file))
        
        # Identify "bad" data (rows with any missing value)
        bad_data = df[df.isnull().any(axis=1)]
        
        # Identify "good" data (rows with no missing values)
        good_data = df.dropna()

        # Sort both dataframes by Date
        if 'Date' in good_data.columns:
            good_data['Date'] = pd.to_datetime(good_data['Date'])
            good_data.sort_values('Date', inplace=True)
            good_data.reset_index(drop=True, inplace=True)

        if 'Date' in bad_data.columns:
            bad_data['Date'] = pd.to_datetime(bad_data['Date'])
            bad_data.sort_values('Date', inplace=True)
            bad_data.reset_index(drop=True, inplace=True)

        # Save cleaned (good) data
        good_data.to_csv(os.path.join(cleaned_data_folder, file), index=False)

        # Save bad data separately if exists
        if not bad_data.empty:
            bad_file_name = f"bad_{file}"
            bad_data.to_csv(os.path.join(bad_data_folder, bad_file_name), index=False)

        print(f"Processed {file}: {len(good_data)} clean rows, {len(bad_data)} bad rows.")