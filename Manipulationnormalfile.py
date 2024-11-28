import pandas as pd
import yfinance as yf
import requests 
import time
from scipy import stats
biglist = pd.read_csv('flat-ui__data-Fri Oct 25 2024.csv')
Tickerlist = biglist['Symbol']
Tickerlist = Tickerlist.to_list()
print(Tickerlist)
revenuegrowth = []
tickerlist = []
ESGratings = []

for i in range(len(Tickerlist)):
    try:
        ticker = yf.Ticker(Tickerlist[i])
        financials = ticker.financials
        revenue = financials.loc["Total Revenue"]
        change = ((revenue.iloc[0]-revenue.iloc[1])/revenue.iloc[0])*100
        revenuegrowth.append(change) 

    except:

        revenuegrowth.append('') 
    try:
        tickerlist.append(Tickerlist[i])
        

    except:
        tickerlist.append('')
        

    try:
        sustainability = ticker.sustainability
        esgrating = sustainability.loc['totalEsg'].values[0]
        ESGratings.append(esgrating)
    except:
        ESGratings.append('')

print(len(ESGratings),len(tickerlist),len(revenuegrowth))
df = pd.DataFrame({
    'Symbol': tickerlist,
    'Revenuegrowth': revenuegrowth,
    "ESG rating": ESGratings 
})
df = df.replace('',pd.NA)
df = df.dropna(subset=['Symbol','Revenuegrowth','ESG rating'], how='any')

df['Revenuegrowth'] = pd.to_numeric(df['Revenuegrowth'], errors='coerce')
df['ESG rating'] = pd.to_numeric(df['ESG rating'], errors='coerce')
df = df.dropna(subset=['Revenuegrowth','ESG rating'])

results = stats.linregress(df['ESG rating'],df['Revenuegrowth'])
df.to_csv('linregressionRevESG.csv') 
