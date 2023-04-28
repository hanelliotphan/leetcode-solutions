# https://leetcode.com/problems/running-sum-of-1d-array/description/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        return nums
