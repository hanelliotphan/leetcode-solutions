# https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

class Solution:
    def numberOfCuts(self, n: int) -> int:
        """
        Logic: Math
        
        Time: O(1)
        Space: O(1)
        """
        if n == 1: return 0
        return n if n % 2 else n // 2
