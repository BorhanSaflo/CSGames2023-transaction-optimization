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

# print(tickerData)

results = []

for key in tickerData:
    values = tickerData[key]
    l = 0   
    maxProfit = 0
    buyDay = 0
    sellDay = 0
    # Increment right ptr every time
    # move left ptr when l > r
    for r in range(1, len(values)):
        if(values[l] > values[r]):
            l = r
        else:
            # Check if max profit is there
            diff = values[r] - values[l]
            if(diff > maxProfit):
                maxProfit = diff
                buyDay = l
                sellDay = r

    results.append([key, maxProfit, buyDay, sellDay])


print(results)


