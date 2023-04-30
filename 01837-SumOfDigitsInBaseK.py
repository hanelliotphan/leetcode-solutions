# https://leetcode.com/problems/sum-of-digits-in-base-k/description/

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        """
        Logic: Divmod
        
        Time: O(n)
        Space: O(1)
        """
        total = 0

        while n:
            n, x = divmod(n, k)
            total += x
        
        return total
