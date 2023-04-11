# https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Logic: Bit Manipulation

        Time: O(n)
        Space: O(1)
        """
        res = 0

        for n in nums:
            res ^= n
        
        return res
