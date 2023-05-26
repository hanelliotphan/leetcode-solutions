# https://leetcode.com/problems/house-robber/description/

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Logic: Dynamic Programming w/ Fibonacci style
        
        Time: O(n)
        Space: O(1)
        """
        rob1, rob2 = 0, 0

        for n in nums:
            total = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = total
        
        return rob2
