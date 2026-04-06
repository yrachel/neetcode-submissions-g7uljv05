class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0

        for curr in prices:
            curr_profit = curr - mini
            if curr_profit > profit:
                profit = curr_profit
            if curr < mini:
                mini = curr
         
        return profit