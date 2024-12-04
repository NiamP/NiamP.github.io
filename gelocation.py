import pandas as pd
import yfinance as yf
import numpy as np

ESGfunds = pd.read_csv('/Users/niampopat/Library/CloudStorage/OneDrive-UniversityofBristol/Documents/Data science for Economists/sustainability.csv')

tickers = ESGfunds['Ticker']
exchanges = []

for i in range(len(ESGfunds)):
    ticker = yf.Ticker(tickers[i])
    fund_info = ticker.info
    exchange = fund_info.get('exchange')
    exchanges.append(exchange)

exchange_country_map = {
    'AMS': 'Netherlands',
    'BER': 'Germany',
    'CPH': 'Denmark',
    'FRA': 'Germany',
    'GER': 'Germany',
    'MCE': 'Spain',
    'MEX': 'Mexico',
    'NAS': 'USA',
    'NGM': 'Sweden',
    'NSI': 'Nigeria',
    'PNK': 'USA',
    'STU': 'Germany',
    'TOR': 'Canada',
}

def getcountry(exchange):
    return exchange_country_map.get(exchange)

countries = []
for i in range(len(exchanges)):
    countries.append(getcountry(exchanges[i]))

ESGfunds['Country'] = countries

ESGfunds.to_csv('Sustainability+country.csv')






    


