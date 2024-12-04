import pandas as pd

df = pd.read_csv('/Users/niampopat/Library/CloudStorage/OneDrive-UniversityofBristol/Documents/Data science for Economists/CSVs/S&P 500 ESG vs Non.csv')

df['Date'] = pd.to_datetime(df['Date'])

df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

df['difference'] = df['S&P 500 ESG'] - df['S&P 500']

reshaped_df = df.melt(id_vars=['Date'], var_name='index', value_name = 'price')

reshaped_df.to_csv('/Users/niampopat/Library/CloudStorage/OneDrive-UniversityofBristol/Documents/Data science for Economists/CSVs/S&P 500 ESG vs Non.csv')

