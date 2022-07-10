class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        """
        Logic: Set length comparison
        
        Time: O(1)
        Space: O(1)
        """
        mn = min(nums)
        mx = max(nums)
        
        return mx-mn+1 == len(nums) == len(set(nums))
