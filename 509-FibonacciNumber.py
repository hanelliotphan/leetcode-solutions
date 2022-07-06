class Solution:
    def fib(self, n: int) -> int:
        """
        Logic: Dynamic Programming top-down
        
        Time: O(n)
        Space: O(1)
        """
        prev, curr = 0, 1
        
        for _ in range(n):
            prev, curr = curr, prev + curr
            
        return prev
