class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        start = 0
        end = 1
        while end <= len(prices)-1:
            new_profit = prices[end] - prices[start]
            if new_profit < 0:
                start = end
                end += 1
            elif new_profit > profit:
                profit = new_profit
                end += 1
            else:
                end += 1
        return profit