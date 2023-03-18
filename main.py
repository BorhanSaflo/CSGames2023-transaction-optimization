# Importing the yfinance package
import yfinance as yf

# Set the start and end date
start_date = '2023-01-01'
end_date = '2023-02-01'

# Set the ticker
tickerList = ['AAl', 'DAL', 'UAL', 'LUV', 'HA']

# Get the data
tickerData = {}

for ticker in tickerList:
    data = yf.download(ticker, start_date, end_date)
    prices = []
    for price in data["Open"]:
        prices.append(price)
    tickerData[ticker] = prices

print(tickerData)


