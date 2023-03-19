import yfinance as yf

budget = 1000000

# Set the start and end date
start_date = '2023-01-01'
end_date = '2023-02-01'

# Set the ticker list
tickerList = ['AAL', 'DAL', 'UAL', 'LUV', 'HA']

# Initialize portfolio with all money in cash
portfolio = {'cash': budget, 'stock': tickerList[0]}

# Track transactions made
transactions = []

# Get the data for each ticker and calculate predicted price increase for each day based on open prices
tickerData = {}
percentChange = {}
for ticker in tickerList:
    data = yf.download(ticker, start_date, end_date)
    prices = []
    for price in data["Open"]:
        prices.append(price)
    tickerData[ticker] = prices
    
    #array of the percent change in price for each day
    percentChange[ticker] = []
    for i in range(1, len(prices)):
        percentChange[ticker].append((prices[i] - prices[i-1]) / prices[i-1])
    

# Loop through each day
for i in range(len(percentChange[tickerList[0]])):
    highestChange = -1
    highestChangeTicker = ""

    for ticker in tickerList:
        if percentChange[ticker][i] > highestChange:
            highestChange = percentChange[ticker][i]
            highestChangeTicker = ticker
    print("The highest change between day " + str(i) + " and day " + str(i+1) + " is " + str(highestChange) + " for " + highestChangeTicker)
        
    
        

    

        
