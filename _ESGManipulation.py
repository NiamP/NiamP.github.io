import pandas as pd
import yfinance as yf

# Load CSV file and filter the top-rated funds based on ESG Score
funds = pd.read_csv('/Users/niampopat/Library/CloudStorage/OneDrive-UniversityofBristol/Documents/Data science for Economists/CSVs/Sustainability+country.csv')
funds = funds.drop(funds.columns[[0, 1]], axis=1)
toprated = funds.nsmallest(50, 'ESG Score')


ticklist = toprated['Ticker'].to_list()

def historicalprices():
    all_data = []
    
    
    for i in range(len(toprated)):
        ticker_symbol = ticklist[i]
        ticker = yf.Ticker(ticker_symbol)

        
        historicaldata = ticker.history(period='5y', interval='1d')

        if not historicaldata.empty:
            
            historicaldata['Ticker'] = ticker_symbol
            
            
            all_data.append(historicaldata[['Close', 'Ticker']])
        else:
            pass
        
       
        if len(all_data) == 5:
            break
    
    # Concatenate all dataframes in the list into one DataFrame
    combined_df = pd.concat(all_data)
    combined_df.reset_index(inplace=True) 
    combined_df['Date'] = pd.to_datetime(combined_df['Date'], utc = True) 
    combined_df['Date'] = combined_df['Date'].dt.tz_localize(None)
    combined_df['Date'] = pd.to_datetime(combined_df['Date']).dt.date

    
    return combined_df

# Get the historical prices DataFrame
prices_df = historicalprices()

# Print the DataFrame
print(prices_df)


prices_df.to_csv('top5prices.csv', index=False)
