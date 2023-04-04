import requests
import json
import pandas as pd
import numpy as np

# Define API endpoint and parameters
url = "https://api.energy.com/data"
params = {
    "start_date": "2022-01-01",
    "end_date": "2022-12-31",
    "location": "California",
    "variables": ["solar", "wind", "hydro"],
    "format": "json"
}

# Send request and retrieve data
response = requests.get(url, params=params)
data = json.loads(response.text)

# Convert data to Pandas DataFrame
df = pd.DataFrame.from_dict(data)

# Calculate total energy production by source
df["total"] = df[["solar", "wind", "hydro"]].sum(axis=1)

# Calculate average daily energy production by source
df["avg_daily_solar"] = df["solar"] / 365
df["avg_daily_wind"] = df["wind"] / 365
df["avg_daily_hydro"] = df["hydro"] / 365

# Calculate average daily total energy production
df["avg_daily_total"] = df["total"] / 365

# Calculate percentage of total energy production by source
df["solar_pct"] = df["solar"] / df["total"] * 100
df["wind_pct"] = df["wind"] / df["total"] * 100
df["hydro_pct"] = df["hydro"] / df["total"] * 100

# Calculate average daily percentage of energy production by source
df["avg_daily_solar_pct"] = df["solar_pct"] / 365
df["avg_daily_wind_pct"] = df["wind_pct"] / 365
df["avg_daily_hydro_pct"] = df["hydro_pct"] / 365

# Calculate average daily percentage of total energy production
df["avg_daily_total_pct"] = df["total"] / df["total"].sum() / 365

# Display results
print(df.head())
