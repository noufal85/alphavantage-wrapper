# Alpha Vantage Wrapper

A Python package that provides a clean, intuitive interface to the Alpha Vantage API.

## Installation

```bash
pip install alphavantage_wrapper
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