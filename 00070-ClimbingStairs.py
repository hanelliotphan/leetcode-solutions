class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Logic: Dynamic Programming (Bottom-Up)
            - Similar to Fibonacci logic
        
        Time: O(n)
        Space: O(1)
        
        Reference: https://www.youtube.com/watch?v=Y0lT9Fck7qI
        """
        curr, prev = 1, 1
        
        for _ in range(n-1):
            prev, curr = curr, curr + prev
        
        return curr
