# Alpha Vantage Wrapper

A Python package that provides a clean, intuitive interface to the Alpha Vantage API.

## Installation

```bash
pip install alphavantage_wrapper
```

## API Key

You need an Alpha Vantage API key to use this package. You can get a free API key at [Alpha Vantage](https://www.alphavantage.co/support/#api-key).

There are two ways to provide your API key:

1. **Directly in code**:
```python
av = AlphaVantage(api_key="YOUR_API_KEY")
```

2. **Using environment variables**:
   - Create a `.env` file in your project root (see `.env.example`)
   - Add your API key: `ALPHA_VANTAGE_API_KEY=your_api_key_here`
   - Load the environment variables (using python-dotenv or similar)
   - Initialize without explicitly providing the key:
```python
# Using python-dotenv
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

av = AlphaVantage()  # API key will be loaded from environment
```

## Usage

```python
from alphavantage_wrapper import AlphaVantage

# Initialize with API key
av = AlphaVantage(api_key="YOUR_API_KEY")

# Get daily stock data as pandas DataFrame
df = av.stocks.daily(symbol="AAPL", outputsize="full")

# Get weekly stock data
weekly_df = av.stocks.weekly(symbol="MSFT")

# Get monthly stock data
monthly_df = av.stocks.monthly(symbol="GOOGL")

# Get intraday stock data
intraday_df = av.stocks.intraday(symbol="AMZN", interval="5min")
```

## Features

- Simple and intuitive API
- Returns pandas DataFrames for easy data manipulation
- Handles API key management securely
- Comprehensive error handling

## License

MIT