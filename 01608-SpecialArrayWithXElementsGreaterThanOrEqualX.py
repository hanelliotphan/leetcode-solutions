# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        Logic: Sorting and Looping X

        Time: O(n*logn)
        Space: O(1)
        """
        nums.sort()

        if len(nums) <= nums[0]:
            return len(nums)

        for i in range(1, len(nums)):
            if nums[i-1] < len(nums)-i <= nums[i]:
                return len(nums)-i
        
        return -1
