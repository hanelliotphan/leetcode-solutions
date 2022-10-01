# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Logic: Sliding Window
        
        Time: O(n)
        Space: O(1)
        """
        l = 0
        n = len(nums)
        
        for r in range(n):
            k -= (1 - nums[r])
            if k < 0:
                k += (1 - nums[l])
                l += 1
                
        return r - l + 1
