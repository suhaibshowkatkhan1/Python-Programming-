import csv

stock_prices = {}

with open('stock_prices.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        symbol = row['Symbol']
        date = row['Date']
        price = float(row['Price'])

        if symbol in stock_prices:
            if price > stock_prices[symbol]['highest']:
                stock_prices[symbol]['highest'] = price
            elif price < stock_prices[symbol]['lowest']:
                stock_prices[symbol]['lowest'] = price
        else:
            stock_prices[symbol] = {'highest': price, 'lowest': price}

for symbol in stock_prices:
    print('stock symbol:', symbol)
    print('Highest price:', stock_prices[symbol]['highest'])
    print('Lowest price:', stock_prices[symbol]['lowest'])
    print()
