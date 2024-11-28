import yfinance as yf
import pandas as pd

biglist = pd.read_csv('flat-ui__data-Fri Oct 25 2024.csv')

Tickerlist = biglist['Symbol']

marketcaps = []
ESGratings = []

for i in range(len(Tickerlist)):
    ticker = yf.Ticker(Tickerlist[i])
    
    try:
        marketcaps.append(ticker.info['marketCap'])

    except:
        marketcaps.append('Unavailable')

    try:
        sustainability = ticker.sustainability
        esgrating = sustainability.loc['totalEsg'].values[0]
        ESGratings.append(esgrating)
    
    except:
        ESGratings.append('Unavailable')

print(len(marketcaps))
print(len(ESGratings))
print(len(Tickerlist))


df = pd.DataFrame({
    'Symbol': Tickerlist,
    'Marketcap': marketcaps,
    'ESG rating': ESGratings
    })
df = df[df['ESG rating'] != 'Unavailable']

df.to_csv('MktCap_vs_ESG.csv', index = False)




