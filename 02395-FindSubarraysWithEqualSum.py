# https://leetcode.com/problems/find-subarrays-with-equal-sum/

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(n)
        """
        visited = set()
        
        for i in range(1, len(nums)):
            if nums[i] + nums[i-1] not in visited:
                visited.add(nums[i] + nums[i-1])
            else:
                return True
            
        return False
