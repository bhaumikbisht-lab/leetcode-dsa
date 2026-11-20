# 121. Best Time to Buy and Sell Stock (Easy) - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Idea: track the cheapest price so far and the best profit from selling today. Time O(n), Space O(1)
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        best = 0
        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > best:
                best = p - min_price
        return best
