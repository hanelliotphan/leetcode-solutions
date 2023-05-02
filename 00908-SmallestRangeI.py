class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        """
        Logic: Mathematical Approach
        
        Time: O(1)
        Space: O(1)
        """
        return max(0, max(nums)-min(nums)-2*k)
