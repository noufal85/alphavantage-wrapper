"""Basic usage examples for the Alpha Vantage API wrapper."""

import os
import pandas as pd
from alphavantage_wrapper import AlphaVantage

# Method 1: Using environment variables directly
print("Method 1: Using environment variables directly")
api_key = os.environ.get("ALPHA_VANTAGE_API_KEY")
if not api_key:
    print("ALPHA_VANTAGE_API_KEY environment variable not set.")
    print("Trying Method 2...")
else:
    # Initialize the client with explicit API key
    av = AlphaVantage(api_key=api_key)
    
    # Get intraday data for Apple
    print("Getting intraday data for AAPL...")
    try:
        intraday_data = av.stocks.intraday(symbol="AAPL", interval="5min")
        print(intraday_data.head())
    except Exception as e:
        print(f"Error: {e}")
    print()

# Method 2: Using python-dotenv to load from .env file
print("Method 2: Using python-dotenv to load from .env file")
try:
    from dotenv import load_dotenv
    load_dotenv()  # Load environment variables from .env file
    
    # Initialize without explicitly providing the key
    av = AlphaVantage()  # API key will be loaded from environment
    
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
except ImportError:
    print("python-dotenv not installed. Install with: pip install python-dotenv")
except Exception as e:
    print(f"Error: {e}")