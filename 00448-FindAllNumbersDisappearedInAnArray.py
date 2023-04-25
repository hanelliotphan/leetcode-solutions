# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Logic: Set Diff
        
        Time: O(n)
        Space: O(n)
        """
        return set(list(range(1, len(nums)+1))) - set(nums)
