import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        max_profit = 0

        for p in prices:
            if p < min_price:
                min_price = p
            if p - min_price > max_profit:
                max_profit =  p - min_price

        return max_profit