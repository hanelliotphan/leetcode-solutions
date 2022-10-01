# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Logic: Sliding Window
        
        Time: O(n)
        Space: O(1)
        """
        all_max = curr_max = sum(nums[:k])
        n = len(nums)
        
        for i in range(k, len(nums)):
            curr_max += (nums[i] - nums[i-k])
            all_max = max(all_max, curr_max)
        
        return all_max / k
