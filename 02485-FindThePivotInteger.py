# https://leetcode.com/problems/find-the-pivot-integer/

class Solution:
    def pivotInteger(self, n: int) -> int:
        """
        Logic: Mathematics
        
        Time: O(1)
        Space: O(1)
        """
        total_sum = n*(n+1) // 2
        return isqrt(total_sum) if isqrt(total_sum)**2 == total_sum else -1 
