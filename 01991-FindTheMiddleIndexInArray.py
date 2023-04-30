# https://leetcode.com/problems/find-the-middle-index-in-array/description/

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        """
        Logic: Two Pointers
        
        Time: O(n)
        Space: O(1)
        """
        l = 0
        r = sum(nums)

        for i, n in enumerate(nums):
            r -= n
            if l == r:
                return i
            l += n
        
        return -1
