# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        count = 0
        
        for i in range(1, len(nums)):
            diff = abs(nums[i]-nums[i-1])
            if nums[i-1] >= nums[i]:
                nums[i] += (diff+1)
                count += (diff+1)
        
        return count
