# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        Logic: Greedy
        
        Time: O(n)
        Space: O(1)
        """
        bought = -prices[0]
        profit = 0

        for p in prices:
            profit = max(profit, bought+p-fee)
            bought = max(bought, profit-p)
        
        return profit
