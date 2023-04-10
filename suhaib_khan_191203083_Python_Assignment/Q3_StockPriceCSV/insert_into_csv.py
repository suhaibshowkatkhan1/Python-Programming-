import csv

with open('stock_prices.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow(['Symbol', 'Date', 'Price'])

    writer.writerow(['AAPL', '2022-01-01', 135.90])
    writer.writerow(['AAPL', '2022-01-02', 138.45])
    writer.writerow(['AAPL', '2022-01-03', 142.20])
    writer.writerow(['GOOG', '2022-01-01', 2105.75])
    writer.writerow(['GOOG', '2022-01-02', 2098.00])
    writer.writerow(['GOOG', '2022-01-03', 2125.50])
    writer.writerow(['MSFT', '2022-01-01', 345.20])
    writer.writerow(['MSFT', '2022-01-02', 344.70])
    writer.writerow(['MSFT', '2022-01-03', 342.10])
