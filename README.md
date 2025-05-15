# Building an Alpha Vantage API Wrapper Package

This document serves as a comprehensive prompt for an LLM to build a Python package that provides easy access to the Alpha Vantage financial data API. The development will follow an incremental approach with clearly defined stages, allowing for systematic implementation and testing.

## Project Overview

Create a Python package named `alphavantage_wrapper` that provides a clean, intuitive interface to the Alpha Vantage API. The package should handle authentication, request formatting, error handling, rate limiting, and data parsing, returning well-structured data in formats convenient for financial analysis (pandas DataFrames where appropriate).

## Implementation Instructions

**IMPORTANT: This is an iterative build process. Follow these instructions strictly:**

1. **Only implement features marked with ✔️** - Features without this mark should not be implemented yet
2. **Use symbols to track progress:**
   - ✔️ = Feature selected for implementation in current iteration
   - ✓ = Feature successfully implemented
   - 🔄 = Feature being updated/refactored from previous implementation
   - ❌ = Feature attempted but has issues that need resolution

3. **Common modules** - Create shared modules for connection handling, error management, rate limiting, and other common functionality that will be reused across different API endpoints

4. **Incremental approach** - Each iteration builds on the previous one. Do not start from scratch each time. Maintain and extend the existing codebase.

5. **Documentation** - Update documentation to reflect the current state of implementation after each iteration

6. **GitHub Integration** - Periodically push updates to the GitHub repository:
   - After completing each feature, commit the changes with a descriptive message
   - After each iteration milestone, create a new release with appropriate version number
   - Use GitHub issues to track bugs and feature requests
   - Repository URL: https://github.com/noufal85/alphavantage-wrapper

## Existing Packages Consideration

Before building from scratch, evaluate these existing packages for potential wrapping or extension:
- `alpha_vantage` (https://github.com/RomelTorres/alpha_vantage)
- `pandas-datareader` (has Alpha Vantage support)
- `alphavantage4py`

If wrapping an existing package, ensure you:
1. Maintain consistent interface design across all endpoints
2. Add missing functionality
3. Improve error handling and documentation
4. Provide additional convenience methods
5. Ensure up-to-date compatibility with the latest Alpha Vantage API

## Development Stages

### Stage 1: Project Setup and Core Functionality
- ✔️ Set up project structure with proper packaging
- ✔️ Implement API key management and configuration
- ✔️ Create base client class with request handling
- [ ] Implement rate limiting and quota management
- [ ] Add comprehensive error handling
- ✔️ Create basic documentation structure

### Stage 2: Stock Time Series API Implementation
- ✓ Implement Intraday Time Series
- ✓ Implement Daily Time Series
- ✔️ Implement Weekly Time Series
- ✔️ Implement Monthly Time Series
- 🔄 Add adjusted vs. unadjusted options
- [ ] Implement Global Quote endpoint
- ❌ Add search functionality
- [ ] Create comprehensive tests for this module

### Stage 3: Fundamental Data API Implementation
- [ ] Implement Company Overview
- [ ] Implement Income Statement
- [ ] Implement Balance Sheet
- [ ] Implement Cash Flow
- [ ] Implement Earnings
- [ ] Add earnings calendar functionality
- [ ] Add IPO calendar functionality
- [ ] Create comprehensive tests for this module

### Stage 4: Technical Indicators Implementation
- ✓ Implement Simple Moving Average (SMA)
- ✓ Implement Exponential Moving Average (EMA)
- ✔️ Implement Weighted Moving Average (WMA)
- [ ] Implement Moving Average Convergence/Divergence (MACD)
- [ ] Implement Relative Strength Index (RSI)
- [ ] Implement Bollinger Bands
- [ ] Implement Stochastic Oscillator
- [ ] Add at least 10 more common technical indicators
- [ ] Create comprehensive tests for this module

### Stage 5: Forex and Cryptocurrency API Implementation
- [ ] Implement Currency Exchange Rates
- [ ] Implement Intraday Forex
- [ ] Implement Daily Forex
- [ ] Implement Weekly Forex
- [ ] Implement Monthly Forex
- [ ] Implement Cryptocurrency Intraday
- [ ] Implement Cryptocurrency Daily
- [ ] Implement Cryptocurrency Weekly
- [ ] Implement Cryptocurrency Monthly
- [ ] Create comprehensive tests for this module

### Stage 6: Economic Indicators and Sector Performance
- [ ] Implement Real GDP
- [ ] Implement Real GDP Per Capita
- [ ] Implement Treasury Yields
- [ ] Implement Federal Funds Rate
- [ ] Implement CPI
- [ ] Implement Inflation
- [ ] Implement Retail Sales
- [ ] Implement Durable Goods Orders
- [ ] Implement Unemployment Rate
- [ ] Implement Nonfarm Payroll
- [ ] Implement Sector Performance
- [ ] Create comprehensive tests for this module

### Stage 7: Advanced Features and Optimization
- [ ] Add async/await support
- [ ] Implement caching mechanism
- [ ] Add batch request functionality where possible
- [ ] Optimize memory usage for large datasets
- [ ] Add export functionality (CSV, Excel, JSON)
- [ ] Implement data visualization helpers
- [ ] Add convenience methods for common financial calculations
- [ ] Create comprehensive tests for these features

### Stage 8: Documentation and Examples
- [ ] Complete API reference documentation
- [ ] Create quickstart guide
- [ ] Add installation instructions
- [ ] Create tutorials for common use cases
- [ ] Add examples for each API category
- [ ] Document best practices and limitations
- [ ] Create Jupyter notebook examples

### Stage 9: Packaging and Distribution
- [ ] Ensure all dependencies are properly specified
- [ ] Create proper package metadata
- [ ] Prepare for PyPI distribution
- [ ] Set up CI/CD pipeline
- [ ] Create release process documentation
- [ ] Publish package to PyPI

## API Endpoints Checklist

### Stock Time Series
- ✔️ TIME_SERIES_INTRADAY
- ✔️ TIME_SERIES_DAILY
- [ ] TIME_SERIES_DAILY_ADJUSTED
- [ ] TIME_SERIES_WEEKLY
- [ ] TIME_SERIES_WEEKLY_ADJUSTED
- [ ] TIME_SERIES_MONTHLY
- [ ] TIME_SERIES_MONTHLY_ADJUSTED
- [ ] GLOBAL_QUOTE
- [ ] SYMBOL_SEARCH

### Fundamental Data
- [ ] OVERVIEW
- [ ] INCOME_STATEMENT
- [ ] BALANCE_SHEET
- [ ] CASH_FLOW
- [ ] EARNINGS
- [ ] EARNINGS_CALENDAR
- [ ] IPO_CALENDAR
- [ ] LISTING_STATUS

### Technical Indicators
- ✓ SMA (Simple Moving Average)
- ✓ EMA (Exponential Moving Average)
- ✔️ WMA (Weighted Moving Average)
- [ ] DEMA (Double Exponential Moving Average)
- [ ] TEMA (Triple Exponential Moving Average)
- [ ] TRIMA (Triangular Moving Average)
- [ ] KAMA (Kaufman Adaptive Moving Average)
- [ ] MAMA (MESA Adaptive Moving Average)
- [ ] T3 (Triple Exponential Moving Average)
- [ ] MACD (Moving Average Convergence/Divergence)
- [ ] MACDEXT (MACD with Controllable Moving Average Type)
- [ ] STOCH (Stochastic Oscillator)
- [ ] STOCHF (Stochastic Fast)
- [ ] RSI (Relative Strength Index)
- [ ] STOCHRSI (Stochastic Relative Strength Index)
- [ ] WILLR (Williams' %R)
- [ ] ADX (Average Directional Movement Index)
- [ ] ADXR (Average Directional Movement Index Rating)
- [ ] APO (Absolute Price Oscillator)
- [ ] PPO (Percentage Price Oscillator)
- [ ] MOM (Momentum)
- [ ] BOP (Balance Of Power)
- [ ] CCI (Commodity Channel Index)
- [ ] CMO (Chande Momentum Oscillator)
- [ ] ROC (Rate of Change)
- [ ] ROCR (Rate of Change Ratio)
- [ ] AROON (Aroon)
- [ ] AROONOSC (Aroon Oscillator)
- [ ] MFI (Money Flow Index)
- [ ] TRIX (1-day Rate of Change of a Triple Smooth EMA)
- [ ] ULTOSC (Ultimate Oscillator)
- [ ] DX (Directional Movement Index)
- [ ] MINUS_DI (Minus Directional Indicator)
- [ ] PLUS_DI (Plus Directional Indicator)
- [ ] MINUS_DM (Minus Directional Movement)
- [ ] PLUS_DM (Plus Directional Movement)
- [ ] BBANDS (Bollinger Bands)
- [ ] MIDPOINT (MidPoint over period)
- [ ] MIDPRICE (Midpoint Price over period)
- [ ] SAR (Parabolic SAR)
- [ ] TRANGE (True Range)
- [ ] ATR (Average True Range)
- [ ] NATR (Normalized Average True Range)
- [ ] AD (Chaikin A/D Line)
- [ ] ADOSC (Chaikin A/D Oscillator)
- [ ] OBV (On Balance Volume)
- [ ] HT_TRENDLINE (Hilbert Transform - Instantaneous Trendline)
- [ ] HT_SINE (Hilbert Transform - SineWave)
- [ ] HT_TRENDMODE (Hilbert Transform - Trend vs Cycle Mode)
- [ ] HT_DCPERIOD (Hilbert Transform - Dominant Cycle Period)
- [ ] HT_DCPHASE (Hilbert Transform - Dominant Cycle Phase)
- [ ] HT_PHASOR (Hilbert Transform - Phasor Components)

### Forex
- [ ] CURRENCY_EXCHANGE_RATE
- [ ] FX_INTRADAY
- [ ] FX_DAILY
- [ ] FX_WEEKLY
- [ ] FX_MONTHLY

### Cryptocurrencies
- [ ] CRYPTO_RATING
- [ ] DIGITAL_CURRENCY_DAILY
- [ ] DIGITAL_CURRENCY_WEEKLY
- [ ] DIGITAL_CURRENCY_MONTHLY
- [ ] DIGITAL_CURRENCY_INTRADAY

### Economic Indicators
- [ ] REAL_GDP
- [ ] REAL_GDP_PER_CAPITA
- [ ] TREASURY_YIELD
- [ ] FEDERAL_FUNDS_RATE
- [ ] CPI
- [ ] INFLATION
- [ ] INFLATION_EXPECTATION
- [ ] CONSUMER_SENTIMENT
- [ ] RETAIL_SALES
- [ ] DURABLES
- [ ] UNEMPLOYMENT
- [ ] NONFARM_PAYROLL

### Sector Performance
- [ ] SECTOR

## Implementation Guidelines

1. **API Key Management**:
   - Support environment variables
   - Allow direct key passing
   - Implement secure storage options

2. **Error Handling**:
   - Provide clear error messages
   - Handle API-specific error codes
   - Implement retry logic for transient errors
   - Handle rate limiting gracefully

3. **Data Formatting**:
   - Return pandas DataFrames by default
   - Support multiple output formats (dict, JSON, CSV)
   - Ensure proper data types (dates as datetime objects, numbers as appropriate numeric types)
   - Handle missing data appropriately

4. **Documentation**:
   - Include docstrings for all public methods
   - Provide examples for each endpoint
   - Document parameters and return values
   - Include type hints

5. **Testing**:
   - Unit tests for all components
   - Integration tests for API interactions
   - Mock responses for testing without API calls
   - Test edge cases and error conditions

6. **Performance Considerations**:
   - Implement caching where appropriate
   - Optimize for memory usage with large datasets
   - Support for async operations
   - Batch operations where possible

## Example Usage (Target API)

```python
# Simple example of desired API
from alphavantage_wrapper import AlphaVantage

# Initialize with API key
av = AlphaVantage(api_key="YOUR_API_KEY")

# Get daily adjusted stock data as pandas DataFrame
df = av.stocks.daily(symbol="AAPL", adjusted=True, outputsize="full")

# Get company overview
overview = av.fundamentals.company_overview(symbol="MSFT")

# Calculate RSI
rsi = av.indicators.rsi(symbol="GOOGL", interval="daily", time_period=14, series_type="close")

# Get currency exchange rate
exchange_rate = av.forex.exchange_rate(from_currency="USD", to_currency="JPY")

# Get cryptocurrency data
bitcoin = av.crypto.daily(symbol="BTC", market="USD")

# Get economic indicator
unemployment = av.economic.unemployment_rate(country="US")
```

## Evaluation Criteria

The final package should be evaluated based on:

1. Completeness of API coverage
2. Code quality and organization
3. Error handling robustness
4. Documentation quality
5. Ease of use
6. Performance
7. Test coverage

## Additional Resources

- Alpha Vantage API Documentation: https://www.alphavantage.co/documentation/
- Python Packaging Guide: https://packaging.python.org/guides/
- Pandas Documentation: https://pandas.pydata.org/docs/
- Requests Library: https://docs.python-requests.org/