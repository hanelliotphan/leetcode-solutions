# https://leetcode.com/problems/create-target-array-in-the-given-order/description/

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1) --> `target` array is required, no extra space needed
        """
        target = []

        for i in range(len(nums)):
            target = target[:index[i]] + [nums[i]] + target[index[i]:]
        
        return target
