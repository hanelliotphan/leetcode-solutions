# https://leetcode.com/problems/number-of-common-factors/

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        """
        Logic: Brute Force
        
        Time: O(min(a,b))
        Space: O(1)
        """
        mn = min(a, b)
        count = 0
        
        for i in range(1, mn+1):
            if a % i == 0 and b % i == 0:
                count += 1
                
        return count
