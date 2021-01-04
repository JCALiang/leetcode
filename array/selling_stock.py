

def maxProfit( prices):
    max_profit = 0
    if not prices:
        return max_profit
    min_cost = prices[0]

    for i in prices:
        if i < min_cost:
            min_cost = i
        elif (i-min_cost) > max_profit:
            max_profit = i-min_cost

    return max_profit



if __name__ == "__main__":
    prices=[7,1,5,3,6,4]
    ans= maxProfit(prices)
    assert ans == 5


''' trick is to track 2 variables:
    min_cost
    and 
    MAX_PROFIT
'''