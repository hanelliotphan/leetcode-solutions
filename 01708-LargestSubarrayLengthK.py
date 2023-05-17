# https://leetcode.com/problems/largest-subarray-length-k/description/

class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        """
        Logic: Brute Force
        
        Time: O(n-k)
        Space: O(1)
        """
        curr_max_idx = 0
        curr_max = float("-inf")
        
        for i in range(len(nums)-k+1):
            if curr_max < nums[i]:
                curr_max = nums[i]
                curr_max_idx = i
        
        return nums[curr_max_idx:curr_max_idx+k]
