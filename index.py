python
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Define API endpoint and parameters
API_URL = "https://api.adx.ae/v1/marketdata"
PARAMS = {
    "api_key": "your_api_key_here",
    "start_date": "2023-01-01",
    "end_date": "2023-12-31",
    "data_type": "market_capitalization"
}

# Fetch data from ADX API
response = requests.get(API_URL, params=PARAMS)
data = response.json()

# Convert data to Pandas DataFrame
df = pd.DataFrame(data["records"])

# Convert date column to datetime type
df["date"] = pd.to_datetime(df["date"])

# Plot Market Capitalization over Time
plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["market_cap"], label="Market Capitalization")
plt.title("ADX Market Capitalization Over Time")
plt.xlabel("Date")
plt.ylabel("Market Capitalization")
plt.legend()
plt.grid()
plt.show()
