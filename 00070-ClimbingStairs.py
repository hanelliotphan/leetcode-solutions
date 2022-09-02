# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Logic: Dynamic Programming (Bottom-Up)
            - Similar to Fibonacci logic
        
        Time: O(n)
        Space: O(1)
        """
        curr, prev = 1, 1
        
        for _ in range(n-1):
            prev, curr = curr, curr + prev
        
        return curr
