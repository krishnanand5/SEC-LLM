import sys
import os
from sec_edgar_downloader import Downloader
import yfinance as yf

def dl_10K_filings(ticker,email_address):
    if not ticker_check(ticker):
        print(f"Invalid ticker symbol : '{ticker}'")
        return
    sec_downloader = Downloader(ticker,email_address)
    sec_downloader.get("10-K",ticker,after="1995-01-01", before="2023-12-31",download_details=True)

def ticker_check(ticker):
    try:
        stock = yf.Ticker(ticker=ticker)
        stock_details = stock.info
        return "quoteType" in stock_details
    except Exception as e:
        print(f"Issue in retrieving info for : {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sec_fetcher.py <Ticker Symbol> <Email Address>")
        sys.exit(1)

    ticker = sys.argv[1].upper()
    email_address = sys.argv[2]
    print(f"Downloading 10-K filings for {ticker} with email address: {email_address}")
    dl_10K_filings(ticker, email_address)