# https://leetcode.com/problems/number-of-zero-filled-subarrays/

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        Logic: Sliding Window
        
        Time: O(n)
        Space: O(1)
        """
        l = 0
        n = len(nums)
        res = 0
        
        for r in range(n):
            if nums[r] == 0:
                res += (r-l+1)
            else:
                l = r + 1
                
        return res
