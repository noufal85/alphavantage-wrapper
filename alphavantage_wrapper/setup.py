from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="alphavantage_wrapper",
    version="0.1.0",
    author="Alpha Vantage Wrapper Team",
    author_email="example@example.com",
    description="A Python wrapper for the Alpha Vantage API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/noufal85/alphavantage-wrapper",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.0",
        "pandas>=1.0.0",
    ],
)