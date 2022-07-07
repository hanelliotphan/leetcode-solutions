class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        """
        Logic: One Pass with increasing/decreasing array check
        
        Time: O(n)
        Space: O(1)
        """
        is_inc = is_desc = True
        
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                is_desc = False
            elif nums[i] > nums[i+1]:
                is_inc = False
                
                
        return is_inc or is_desc
