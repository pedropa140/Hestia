import requests
import json
import csv
import pandas as pd
import numpy as np
import time
from datetime import timedelta
from quarterly_report import QuarterlyReport
from pandas.tseries.holiday import USFederalHolidayCalendar

additonal_info_sic = dict()
additonal_info_mc = dict()


def get_financials(api_key, ticker):
    url = "https://api.polygon.io/vX/reference/financials"
    params = {
        "ticker": ticker,
        "timeframe": "quarterly",
        "limit": 100,
        "apiKey": api_key
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for any HTTP error
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

def fetch_price_data(api_key, ticker, date):
    url = f'https://api.polygon.io/v3/open-close/{ticker}/{date}?adjusted=true&apiKey={api_key}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('open', np.nan), data.get('close', np.nan), data.get('high', np.nan), data.get('low', np.nan)
        elif response.status_code == 403:
            return np.nan, np.nan, np.nan, np.nan
        else: 
            print(f"Failed to fetch price data for {ticker} on {date}. Status code: {response.status_code}")
            return np.nan, np.nan, np.nan, np.nan
    except Exception as e:
        print(f"An error occurred while fetching price data: {e}")
        return np.nan, np.nan, np.nan, np.nan

def read_api_key_from_config():
    try:
        with open('config.json') as f:
            config_data = json.load(f)
            return config_data['api_key']
    except Exception as e:
        print(f"An error occurred while reading API key from config file: {str(e)}")
        return None

def closest_trading_day(date):
    cal = USFederalHolidayCalendar()
    
    us_holidays = cal.holidays(start=pd.Timestamp(date) - pd.DateOffset(years=5), end=pd.Timestamp(date))


    date = pd.Timestamp(date)


    delta_before = delta_after = timedelta(days=1)

  
    while str(date - delta_before)[:10] in us_holidays or (date - delta_before).weekday() >= 5:
        delta_before += timedelta(days=1)
    while str(date + delta_after)[:10] in us_holidays or (date + delta_after).weekday() >= 5:
        delta_after += timedelta(days=1)


    diff_before = (date - delta_before) - date
    diff_after = (date + delta_after) - date
    if diff_before < diff_after:
        return str(date - delta_before)[:10]
    else:
        return str(date + delta_after)[:10]

def read_tickers_csv(file_path):
    tickers = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:  # Assuming each row contains ticker and name
                tickers.append((row[0], row[1]))
    return tickers

def get_quarterly_reports():
    api_key = read_api_key_from_config()
    if api_key is None:
        return
    
    tickers = read_tickers_csv("tickers_with_dividends.csv")
    quarterly_reports = []
    dfs = []
    
    count = 0
    for ticker in tickers:
        ticker_total = []
        total_df = []
        print(f'on item {count} of {len(tickers)}')
        results = get_financials(api_key, ticker[0])
        print(f'working on ticker {ticker[0]}')
        if results is None:
            continue
        for result in results['results']:
            qr = QuarterlyReport(result)
            
            ticker = qr.ticker
            s_date = closest_trading_day(qr.start_date)
            e_date = closest_trading_day(qr.end_date)

            s_open, s_close, s_high, s_low = fetch_price_data(api_key, ticker, s_date)
            e_open, e_close, e_high, e_low = fetch_price_data(api_key, ticker, e_date)
            qr.set_start_prices(s_open, s_close, s_high, s_low)
            qr.set_end_prices(e_open, e_close, e_high, e_low)
            qr.calculate_dividend_yield_ratio(s_open)
            
            quarterly_reports.append(qr)
            ticker_total.append(qr)
        for qr in ticker_total:
            df_temp = qr.get_df()
            total_df.append(df_temp)
        print(len(total_df))
        if(not len(total_df) <= 1):
            combined_df = pd.concat(total_df, ignore_index=True)
            combined_df.to_csv(f'./div_info/{ticker}.csv', index=False)
        count += 1

    for qr in quarterly_reports:
        df = qr.get_df()
        dfs.append(df)
    
    
    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df.to_csv('combined_quarterly_reports.csv', index=False)
    
    return quarterly_reports


def get_market_cap(ticker):
    api_url = f"https://api.polygon.io/v3/reference/tickers/{ticker}?date=2024-04-08&apiKey=1023s0ZC9ogHepq151jtapaFSdNV9mi4"
    if(ticker in additonal_info_mc):
        return additonal_info_mc[ticker]
    print(ticker)
    time.sleep(.25)
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()['results']
        market_cap = data.get('market_cap', None)
        additonal_info_mc[ticker] = market_cap
        return market_cap
    else:
        print(f"Failed to retrieve data for {ticker}. Status code: {response.status_code} : {response}")
        return None

def get_sic_code(ticker):
    api_url = f"https://api.polygon.io/v3/reference/tickers/{ticker}?date=2024-04-08&apiKey=1023s0ZC9ogHepq151jtapaFSdNV9mi4"
    if(ticker in additonal_info_sic):
        return additonal_info_sic[ticker]
    print(ticker)
    time.sleep(.25)
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()['results']
        sic_code = data.get('sic_description', None)
        additonal_info_sic[ticker] =  sic_code
        return sic_code
    else:
        print(f"Failed to retrieve data for {ticker}. Status code: {response.status_code} : {response}")
        return None

def categorize_market_cap(market_cap):
    if market_cap is None:
        return None
    elif market_cap > 200e9:
        return 'Mega-cap'
    elif 10e9 <= market_cap <= 200e9:
        return 'Large-cap'
    elif 2e9 <= market_cap < 10e9:
        return 'Mid-cap'
    elif 250e6 <= market_cap < 2e9:
        return 'Small-cap'
    else:
        return 'Micro-cap'

def categorize_indicator(price_movement_percent):
    if price_movement_percent is None:
        return None
    elif price_movement_percent <= .05 and price_movement_percent >= -.05:
        return 0
    elif price_movement_percent > .05 :
        return 1
    else:
        return -1


def calculate_percentage_movement(df):
    df['start_open'] = pd.to_numeric(df['start_open'], errors='coerce')
    df['start_close'] = pd.to_numeric(df['start_close'], errors='coerce')
    df['end_open'] = pd.to_numeric(df['end_open'], errors='coerce')
    df['end_close'] = pd.to_numeric(df['end_close'], errors='coerce')

    df['price_movement_percent'] = ((df['end_close'] - df['start_open']) / df['start_open'])
    return df

def main():
    df = pd.read_csv('full_combined_quarterly_reports.csv')
    if(df is None):
        df = get_quarterly_reports()
        df['market_cap']= df['ticker'].apply(get_market_cap)
       
        df['market_cap_category'] = df['market_cap'].apply(categorize_market_cap)
        print(df)
    df = calculate_percentage_movement(df)
    df['sic_code'] = df['ticker'].apply(get_sic_code)
    df['indicator'] = df['price_movement_percent'].apply(categorize_indicator)
    df.to_csv('full_combined_quarterly_reports.csv', index=False)





if __name__ == "__main__":
    main()
