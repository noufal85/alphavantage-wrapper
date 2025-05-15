"""Basic usage examples for the Alpha Vantage API wrapper."""

import os
import pandas as pd
from alphavantage_wrapper import AlphaVantage

# Get API key from environment variable
api_key = os.environ.get("ALPHA_VANTAGE_API_KEY")
if not api_key:
    print("Please set the ALPHA_VANTAGE_API_KEY environment variable.")
    exit(1)

# Initialize the client
av = AlphaVantage(api_key=api_key)

# Get intraday data for Apple
print("Getting intraday data for AAPL...")
intraday_data = av.stocks.intraday(symbol="AAPL", interval="5min")
print(intraday_data.head())
print()

# Get daily data for Microsoft
print("Getting daily data for MSFT...")
daily_data = av.stocks.daily(symbol="MSFT")
print(daily_data.head())
print()

# Get weekly data for Google
print("Getting weekly data for GOOGL...")
weekly_data = av.stocks.weekly(symbol="GOOGL")
print(weekly_data.head())
print()

# Get monthly data for Amazon
print("Getting monthly data for AMZN...")
monthly_data = av.stocks.monthly(symbol="AMZN")
print(monthly_data.head())
print()