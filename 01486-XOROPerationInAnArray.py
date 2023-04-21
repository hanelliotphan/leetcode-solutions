# https://leetcode.com/problems/xor-operation-in-an-array/description/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        res = start
        i = 1

        while i < n:
            res ^= (start+2*i)
            i += 1
        
        return res
