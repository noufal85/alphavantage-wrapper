"""Configuration module for Alpha Vantage API wrapper.

This module handles API key management and other configuration options.
"""

import os
from typing import Optional


class Config:
    """Configuration class for Alpha Vantage API wrapper."""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize configuration with API key.

        Args:
            api_key: Alpha Vantage API key. If not provided, will look for
                    ALPHA_VANTAGE_API_KEY environment variable.
        """
        self._api_key = api_key or os.environ.get("ALPHA_VANTAGE_API_KEY")
        if not self._api_key:
            raise ValueError(
                "API key must be provided either as an argument or "
                "as ALPHA_VANTAGE_API_KEY environment variable."
            )

    @property
    def api_key(self) -> str:
        """Get the API key."""
        return self._api_key

    @api_key.setter
    def api_key(self, value: str) -> None:
        """Set the API key."""
        if not value:
            raise ValueError("API key cannot be empty.")
        self._api_key = value

    def get_base_params(self) -> dict:
        """
        Get base parameters for API requests.

        Returns:
            Dictionary with base parameters including API key.
        """
        return {"apikey": self._api_key}