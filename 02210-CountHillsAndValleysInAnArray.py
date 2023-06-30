# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        prev = nums[0]
        count = 0

        for i in range(1, len(nums)-1):
            if prev < nums[i] and nums[i] > nums[i+1]:
                count += 1
            elif prev > nums[i] and nums[i] < nums[i+1]:
                count += 1
            if nums[i] != nums[i+1]:
                prev = nums[i]
        
        return count
