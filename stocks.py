import requests
import json
import csv

apiKey = "c9sdv8qad3i4aps1sleg"

# Ticker symbols for each stock
symbols = ["AAPL", "AMZN", "NFLX", "GOOG", "FB"]

base_url="https://finnhub.io/api/v1/quote?"
stocks = {}
stocks_change = {}

# Iterate through the symbols list and get the quote and percentage change for each stock
for i in symbols:
    r = requests.get(base_url, params = {'symbol':i,'token':apiKey})
    text = r.text
    
    stock = json.loads(text)
    stocks[i] = stock
    stocks_change[i] = stock["dp"]

greatest_change = max(stocks_change, key=stocks_change.get)

# Return the stock with the greatest change from the stocks dictionary
most_volatile_stock = (stocks[greatest_change])

# Data rows for the csv file
stock_symbol = greatest_change
percentage_change = most_volatile_stock["dp"]
current_price = most_volatile_stock["c"]
last_close_price= most_volatile_stock["pc"]

# Column headings for the csv file
csv_columns = ['stock_symbol','percentage_change','current_price', "last_close_price"]

# Data to write to csv file
csv_rows = [stock_symbol, percentage_change, current_price, last_close_price]
csv_file = "stocks.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_columns)
        writer.writerow(csv_rows)
except IOError:
    print("I/O error")