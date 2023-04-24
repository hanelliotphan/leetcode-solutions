class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        closest = abs(nums[0])
        largest = nums[0]
        
        for n in nums:
            if abs(n) < closest:
                closest = abs(n)
                largest = n
            elif abs(n) == closest:
                largest = max(largest, n)
        
        return largest
