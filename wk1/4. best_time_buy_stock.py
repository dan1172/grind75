def maxProfit(self, prices: List[int]) -> int:
    cheapest = prices[0]
    max_profit = 0
    for p in prices:
        if p - cheapest > max_profit:
            max_profit = p - cheapest
        if p < cheapest:
            cheapest = p
    return max_profit