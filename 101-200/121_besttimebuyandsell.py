def maxProfit(prices):
    cheapest = float('inf')
    maxProfit = 0

    for price in prices:
        cheapest = min(cheapest, price)
        if price - cheapest > maxProfit:
            maxProfit = price - cheapest
    
    return maxProfit