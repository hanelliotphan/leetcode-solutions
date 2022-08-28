class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        """
        Logic: Set Intersection
        
        Time: O(n)
        Space: O(n1) --> n1 = len(nums[0])
        """
        n_array = nums[0]
        
        for i in range(1, len(nums)):
            n_array = set(n_array) & set(nums[i])
            
        return sorted(n_array)
