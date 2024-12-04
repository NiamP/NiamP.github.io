import yfinance as yf 
import pandas as pd
import re

# Create a new variable with extracted tickers from MutualFUndList csv file 
Mutualfunds = pd.read_csv("MutualFundList.csv",)
Tickers = Mutualfunds['Unnamed: 0']
cleanedTickers = Tickers.dropna()


# create a function to ge tthe sustainability scores for each ticker
def getsustainabilityscore():
    tickerlist = []
    totalesglist = []

    
    for i in range(len(cleanedTickers)):
        # use try and except in case data is not available for a given ticker
        try:
            ticker = yf.Ticker(cleanedTickers[i])
            
            esg_scores = ticker.sustainability
            totalesg = esg_scores.loc['totalEsg']
            tickerlist.append(ticker)
            totalesglist.append(totalesg)

            
        except:
            pass

    df = pd.DataFrame({'Ticker': tickerlist, 'Total ESG': totalesglist})
    return(df)

#present this data as a new csv file 
x = getsustainabilityscore()
x.to_csv('sustainability.csv')

#Now need to clean up the CSV to just contain the ticker and its score

df = pd.read_csv('sustainability.csv')


tickers = []
esg_scores = []


for index, row in df.iterrows():
    # Extract the ticker 
    ticker_match = re.search(r'<(.*?)>', row['Ticker'])
    if ticker_match:
        tickers.append(ticker_match.group(1))
    
    # Extract the ESG score 
    esg_match = re.search(r'esgScores\s+([0-9.]+)', row['Total ESG'])
    if esg_match:
        esg_scores.append(float(esg_match.group(1)))

# Create a new DataFrame with the extracted values
extracted_data = pd.DataFrame({
    'Ticker': tickers,
    'ESG Score': esg_scores
})

# Overwrite the current csv file with the new cleaned one
extracted_data.to_csv('sustainability.csv')





