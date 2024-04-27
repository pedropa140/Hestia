import csv
import json
import requests
import os
import pandas as pd
import numpy as np
from urllib.parse import urlparse, parse_qs, urlencode

def fetch_tickers(api_key):
    tickers = set()
    next_url = f'https://api.polygon.io/v3/reference/tickers?type=CS&market=stocks&active=true&limit=1000&apiKey={api_key}'
    while next_url:
        try:
            response = requests.get(next_url)
            if response.status_code == 200:
                data = response.json()
                if not data['results']:
                    break  # No more tickers available, exit the loop
                for result in data['results']:
                    tickerInfo = (result['ticker'], result['name'])
                    tickers.add(tickerInfo)
                next_url = append_api_key_to_url(data['next_url'], api_key)
            else:
                print(f"Error: {response.status_code} - {response.text}")
                break
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            break
    return tickers

def fetch_dividend_data(api_key, ticker):
    url = f'https://api.polygon.io/v3/reference/dividends?ticker={ticker}&limit=1000&apiKey={api_key}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('results', [])  # Return an empty list if 'results' key is not present
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def fetch_price_data(api_key, ticker, date):
    url = f'https://api.polygon.io/v1/open-close/{ticker}/{date}?adjusted=true&apiKey={api_key}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('open', np.nan), data.get('close', np.nan), data.get('high', np.nan), data.get('low', np.nan)
        else:
            print(f"Failed to fetch price data for {ticker} on {date}. Status code: {response.status_code}")
            return np.nan, np.nan, np.nan, np.nan
    except Exception as e:
        print(f"An error occurred while fetching price data: {e}")
        return np.nan, np.nan, np.nan, np.nan

def append_api_key_to_url(url, api_key):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    query_params['apiKey'] = api_key
    updated_query = urlencode(query_params, doseq=True)
    return f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?{updated_query}"

def write_tickers_with_dividends_to_csv(tickers_with_dividends, filename):
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Ticker', 'Name'])
            for tickerInfo in tickers_with_dividends:
                writer.writerow(tickerInfo)
        print(f"Successfully wrote tickers with dividend info to {filename}")
    except Exception as e:
        print(f"An error occurred while writing tickers to CSV: {str(e)}")

def read_api_key_from_config():
    try:
        with open('config.json') as f:
            config_data = json.load(f)
            return config_data['api_key']
    except Exception as e:
        print(f"An error occurred while reading API key from config file: {str(e)}")
        return None

def main():
    api_key = read_api_key_from_config()

    if api_key:
        # Step 1: Fetch tickers
        tickers = fetch_tickers(api_key)
        if tickers:
            tickers_with_dividends = []

            # Step 2: Fetch dividend data for each ticker and price data
            for tickerInfo in tickers:
                ticker, name = tickerInfo
                dividend_data = fetch_dividend_data(api_key, ticker)
                if dividend_data:  # Check if dividend_data is not empty
                    tickers_with_dividends.append(tickerInfo)

            # Step 3: Write tickers with dividend info to CSV
            tickers_with_dividends_filename = 'tickers_with_dividends.csv'
            write_tickers_with_dividends_to_csv(tickers_with_dividends, tickers_with_dividends_filename)
        else:
            print("No tickers fetched.")
    else:
        print("API key not found in config file.")

if __name__ == "__main__":
    main()
