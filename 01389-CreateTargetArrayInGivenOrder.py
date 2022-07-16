class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        """
        Logic: Zip & insert
        
        Time: O(n)
        Space: O(1) -- target is required, no extra space needed
        """
        target = []
        
        for n, i in zip(nums, index):
            target.insert(i, n)
        
        return target
