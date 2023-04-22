# https://leetcode.com/problems/ugly-number/description/

class Solution:
    def isUgly(self, n: int) -> bool:
        """
        Logic: Brute Force
        
        Time: O(logp(n))
        Space: O(1)
        """
        for p in [2, 3, 5]:
            while n % p == 0 and n % p < n:
                n //= p
        
        return n == 1
