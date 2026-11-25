# 322. Coin Change (Medium) — Day 7, 2026-11-25
# Idea: dp[a] = min coins for amount a; try every coin as the last one used.
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a - c] + 1)
        return dp[amount] if dp[amount] != INF else -1
# Time: O(amount x coins) | Space: O(amount)
