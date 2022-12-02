# https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        """
        Logic: Brute Force
        
        Time: O(n*logn)
        Space: O(1)
        """
        # Apply operations
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        # Return `nums` after pushing all the 0s to the end
        return sorted(nums, key=lambda x: not x)
