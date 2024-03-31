def maxProfit(prices):
    cheapest = prices[0] # First price is always the cheapest so far
    maxProfit = 0

    for price in prices:
        if price < cheapest:
            cheapest = price
        
