class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # first val becomes the min right away
        # move on to the next, if next val is less than curr val, then next val is curr min
        # if next val is more than curr val then sell, record profit 
        # next val becomes min if less than min 
        # greater profit is replaced if higher than curr profit
        len_prices = len(prices)
        curr_min = prices[0]
        profit = 0
        for i in range(1, len_prices):
            if prices[i] < curr_min:
                curr_min = prices[i]
            elif prices[i] > curr_min:
                new_profit = prices[i] - curr_min
                if new_profit > profit:
                    profit = new_profit
                else:
                    continue
        return profit

