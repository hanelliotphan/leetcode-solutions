# https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        """
        Logic: Dynamic Programming (Optimized)
        
        Time: O(n)
        Space: O(1)
        """
        if n == 0: return 0
        if n < 3: return 1

        t0 = 0
        t1 = t2 = 1

        for _ in range(n-2):
            t0, t1, t2 = t1, t2, t0+t1+t2
        
        return t2
