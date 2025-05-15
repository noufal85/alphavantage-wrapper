"""Base client for Alpha Vantage API wrapper.

This module provides the base client class for making requests to the Alpha Vantage API.
"""

import requests
from typing import Dict, Any, Optional
import pandas as pd

from .config import Config
from .stocks import StockTimeSeries


class AlphaVantage:
    """Main client class for Alpha Vantage API."""

    BASE_URL = "https://www.alphavantage.co/query"

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Alpha Vantage client.

        Args:
            api_key: Alpha Vantage API key. If not provided, will look for
                    ALPHA_VANTAGE_API_KEY environment variable.
        """
        self.config = Config(api_key)
        self.stocks = StockTimeSeries(self)

    def _make_request(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Make a request to the Alpha Vantage API.

        Args:
            params: Parameters for the request.

        Returns:
            JSON response from the API.

        Raises:
            requests.exceptions.RequestException: If the request fails.
            ValueError: If the API returns an error message.
        """
        # Add API key to parameters
        params.update(self.config.get_base_params())

        # Make the request
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse the response
        data = response.json()

        # Check for error messages
        if "Error Message" in data:
            raise ValueError(f"API Error: {data['Error Message']}")
        if "Information" in data and "Note" in data:
            # This is usually a rate limit warning, but we'll just print it
            print(f"API Note: {data['Note']}")

        return data