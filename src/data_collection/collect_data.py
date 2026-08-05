import yfinance as yf
import pandas as pd

print("Downloading ICLN data...")

data = yf.download(
    "ICLN",
    start="2015-01-01",
    end="2026-01-01"
)

print(data.head())

data.to_csv(
    "data/raw/icln_prices.csv"
)

print("Finished")
