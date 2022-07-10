class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        """
        Logic: Straightforward  
        
        Time: O(n)
        Space: O(1)
        """
        curr_closest = nums[0]
        
        for n in nums:
            if abs(n) < abs(curr_closest) \
            or (abs(n) ==  abs(curr_closest) and curr_closest <= n):
                curr_closest = n
        
        return curr_closest
