# https://leetcode.com/problems/smallest-even-multiple/

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        """
        Logic: Brute Force
        
        Time: O(1)
        Space: O(1)
        """
        if n % 2 == 0:
            return n
        
        return 2*n
