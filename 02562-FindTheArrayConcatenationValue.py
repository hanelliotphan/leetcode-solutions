# https://leetcode.com/problems/find-the-array-concatenation-value/description/

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        """
        Logic: Two Pointers

        Time: O(n)
        Space: O(1)
        """
        res = 0 
        i = 0; j = len(nums)-1

        while i < j:
            res += int(str(nums[i])+str(nums[j]))
            i += 1
            j -= 1
        
        if i == j:
            res += nums[i]
        
        return resa
