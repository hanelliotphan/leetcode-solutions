# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(n)
        """
        visited = set()
        i = 0

        while i < len(nums):
            if nums[i] in visited:
                nums.pop(i)
            else:
                visited.add(nums[i])
                i += 1

        return len(nums)
