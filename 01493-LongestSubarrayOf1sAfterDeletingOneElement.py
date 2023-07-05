# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Logic: Sliding Window (influenced by the problem #1004 - Max Consecutive Ones III)

        Time: O(n)
        Space: O(1)
        """
        l = 0
        n = len(nums)
        k = 1
        
        for r in range(n):
            k -= (1 - nums[r])
            if k < 0:
                k += (1 - nums[l])
                l += 1
                
        return r - l
