class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Logic: Straightforward loop
        
        Time: O(n)
        Space: O(1) -- reuse the parsed-in array
        """
        total = nums[0]
        
        for i in range(1, len(nums)):
            nums[i] += total
            total = nums[i]
            
        return nums
