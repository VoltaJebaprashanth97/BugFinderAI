import pandas as pd
from bs4 import BeautifulSoup
import shutil

import Config

input_csv_path = Config.RAW_CSV_PATH
df = pd.read_csv(input_csv_path)


# ------------------------------------------- HTML TAG REMOVING -------------------------------------------


def remove_html_tags(value):
    if isinstance(value, str):
        soup = BeautifulSoup(value, 'html.parser')
        text = soup.get_text(separator='\n', strip=True)
        return text
    else:
        return value


# Remove HTML Tags and clean the Data
df = df.applymap(remove_html_tags)

# --------------------------------------------- Checking ID is number ----------------------------------------

# Convert the "ID" column to numeric, coerce errors to NaN for non-numeric values
df['ID'] = pd.to_numeric(df['ID'], errors='coerce')

# Filter out rows where "ID" is not a valid integer
df = df[pd.notna(df['ID']) & (df['ID'] % 1 == 0)].astype({'ID': int})

# --------------------------------------------- Cleaning Other fields --------------------------------------

# Assuming df is your DataFrame
values_to_remove = ['-',
                    '',
                    'any relevant values you need to remove'
                    ]

# Use the ~ operator to negate the condition
df = df[~df['Project Code'].apply(lambda x: x in values_to_remove)].copy()


# --------------------------------------------- Convert Date Time -----------------------------------------

def extract_date_components(date_string):
    date_parts = date_string.split(" ")
    month_str = date_parts[1]
    day_str = date_parts[2]
    year_str = date_parts[3]

    # Convert month string to month number
    month_number = pd.to_datetime(month_str, format='%b').month

    # Convert strings to numbers
    day_number = int(day_str)
    year_number = int(year_str)

    # Combine components into a single datetime64 column
    result_date = pd.to_datetime(f"{year_number}-{month_number:02d}-{day_number:02d} {date_parts[4]}")

    return result_date


# Apply the method to the "Created Date" column
df['Created Date'] = df['Created Date'].apply(extract_date_components)

# --------------------------------------------- Write to new CSV --------------------------------------------------

# Write the DataFrame to a CSV file
output_csv_path = Config.CLEANED_CSV_PATH
df.to_csv(output_csv_path, index=False)
