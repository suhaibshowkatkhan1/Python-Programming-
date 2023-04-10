def Best_Buying_Selling_Day(stock_prices):
    n = len(stock_prices)
    maximum_profit = 0
    buying_day = 0
    selling_day = 0

    for i in range(n):
        for j in range(i + 1, n):
            profit = stock_prices[j] - stock_prices[i]
            if profit > maximum_profit:
                maximum_profit = profit
                buying_day = i
                selling_day = j

    return buying_day, selling_day


stock_prices = [100, 180, 260, 310, 400, 535, 695]
best_days = Best_Buying_Selling_Day(stock_prices)
print("Best day for buying Stock is: day", best_days[0] + 1, "(price=", stock_prices[best_days[0]], ")")
print("Best days to sell your stock is: day", best_days[1] + 1, "(price=", stock_prices[best_days[1]], ")")
