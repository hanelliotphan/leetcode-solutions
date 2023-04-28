# https://leetcode.com/problems/largest-perimeter-triangle/description/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        Logic: Mathematical Approach + Sort
        
        Time: O(n)
        Space: O(1)
        """
        nums.sort()

        for i in range(len(nums)-3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        
        return 0
