"""Stock Time Series module for Alpha Vantage API wrapper.

This module provides access to the Stock Time Series endpoints of the Alpha Vantage API.
"""

from typing import Dict, Any, Optional
import pandas as pd


class StockTimeSeries:
    """Stock Time Series API endpoints."""

    def __init__(self, client):
        """
        Initialize Stock Time Series API.

        Args:
            client: Alpha Vantage client instance.
        """
        self._client = client

    def intraday(
        self,
        symbol: str,
        interval: str = "5min",
        adjusted: bool = True,
        outputsize: str = "compact",
        datatype: str = "json",
    ) -> pd.DataFrame:
        """
        Get intraday time series for a stock.

        Args:
            symbol: The stock symbol.
            interval: Time interval between data points. One of: 1min, 5min, 15min, 30min, 60min.
            adjusted: Whether to return adjusted data.
            outputsize: Size of the returned data. 'compact' returns the latest 100 data points,
                        'full' returns up to 20 years of historical data.
            datatype: Data format. 'json' or 'csv'.

        Returns:
            Pandas DataFrame with the intraday time series.
        """
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": interval,
            "adjusted": "true" if adjusted else "false",
            "outputsize": outputsize,
            "datatype": datatype,
        }

        data = self._client._make_request(params)
        
        # Extract the time series data
        time_series_key = f"Time Series ({interval})"
        if time_series_key not in data:
            raise ValueError(f"No time series data found for {symbol} with interval {interval}")
        
        # Convert to DataFrame
        df = pd.DataFrame.from_dict(data[time_series_key], orient="index")
        
        # Convert column names
        df.columns = [col.split(". ")[1] for col in df.columns]
        
        # Convert index to datetime
        df.index = pd.to_datetime(df.index)
        
        # Convert values to float
        for col in df.columns:
            df[col] = pd.to_numeric(df[col])
        
        return df

    def daily(
        self,
        symbol: str,
        outputsize: str = "compact",
        datatype: str = "json",
    ) -> pd.DataFrame:
        """
        Get daily time series for a stock.

        Args:
            symbol: The stock symbol.
            outputsize: Size of the returned data. 'compact' returns the latest 100 data points,
                        'full' returns up to 20 years of historical data.
            datatype: Data format. 'json' or 'csv'.

        Returns:
            Pandas DataFrame with the daily time series.
        """
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "outputsize": outputsize,
            "datatype": datatype,
        }

        data = self._client._make_request(params)
        
        # Extract the time series data
        time_series_key = "Time Series (Daily)"
        if time_series_key not in data:
            raise ValueError(f"No daily time series data found for {symbol}")
        
        # Convert to DataFrame
        df = pd.DataFrame.from_dict(data[time_series_key], orient="index")
        
        # Convert column names
        df.columns = [col.split(". ")[1] for col in df.columns]
        
        # Convert index to datetime
        df.index = pd.to_datetime(df.index)
        
        # Convert values to float
        for col in df.columns:
            df[col] = pd.to_numeric(df[col])
        
        return df

    def weekly(
        self,
        symbol: str,
        datatype: str = "json",
    ) -> pd.DataFrame:
        """
        Get weekly time series for a stock.

        Args:
            symbol: The stock symbol.
            datatype: Data format. 'json' or 'csv'.

        Returns:
            Pandas DataFrame with the weekly time series.
        """
        params = {
            "function": "TIME_SERIES_WEEKLY",
            "symbol": symbol,
            "datatype": datatype,
        }

        data = self._client._make_request(params)
        
        # Extract the time series data
        time_series_key = "Weekly Time Series"
        if time_series_key not in data:
            raise ValueError(f"No weekly time series data found for {symbol}")
        
        # Convert to DataFrame
        df = pd.DataFrame.from_dict(data[time_series_key], orient="index")
        
        # Convert column names
        df.columns = [col.split(". ")[1] for col in df.columns]
        
        # Convert index to datetime
        df.index = pd.to_datetime(df.index)
        
        # Convert values to float
        for col in df.columns:
            df[col] = pd.to_numeric(df[col])
        
        return df

    def monthly(
        self,
        symbol: str,
        datatype: str = "json",
    ) -> pd.DataFrame:
        """
        Get monthly time series for a stock.

        Args:
            symbol: The stock symbol.
            datatype: Data format. 'json' or 'csv'.

        Returns:
            Pandas DataFrame with the monthly time series.
        """
        params = {
            "function": "TIME_SERIES_MONTHLY",
            "symbol": symbol,
            "datatype": datatype,
        }

        data = self._client._make_request(params)
        
        # Extract the time series data
        time_series_key = "Monthly Time Series"
        if time_series_key not in data:
            raise ValueError(f"No monthly time series data found for {symbol}")
        
        # Convert to DataFrame
        df = pd.DataFrame.from_dict(data[time_series_key], orient="index")
        
        # Convert column names
        df.columns = [col.split(". ")[1] for col in df.columns]
        
        # Convert index to datetime
        df.index = pd.to_datetime(df.index)
        
        # Convert values to float
        for col in df.columns:
            df[col] = pd.to_numeric(df[col])
        
        return df