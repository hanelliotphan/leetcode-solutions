class Solution:
    def fib(self, n: int) -> int:
        """
        Logic: Dynamic Programming top-down
        
        Time: O(n)
        Space: O(1)
        """
        if 0 < n <= 2:
            return 1
        elif n == 0:
            return 0
        
        curr = prev = 1

        for _ in range(n-2):
            curr, prev = curr+prev, curr
        
        return curr
