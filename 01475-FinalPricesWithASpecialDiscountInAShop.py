# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        Logic: One Pass with Stack
        
        Time: O(n)
        Space: O(n)
        """
        stack = []

        for i, n in enumerate(prices):
            while stack and prices[stack[-1]] >= n:
                prices[stack.pop()] -= n
            stack.append(i)
        
        return prices
