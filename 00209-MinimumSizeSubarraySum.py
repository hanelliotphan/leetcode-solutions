# https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Logic: Sliding Window

        Time: O(n)
        Space: O(1)
        """
        start = 0
        curr_window_sum = 0
        l = float("inf")

        for curr in range(len(nums)):
            curr_window_sum += nums[curr]
            while curr_window_sum >= target:
                l = min(l, curr-start+1)
                curr_window_sum -= nums[start]
                start += 1
        
        return l if l != float("inf") else 0
