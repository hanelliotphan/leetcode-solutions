# https://leetcode.com/problems/array-partition/description/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        """
        Logic: Sorting

        Time: O(n*logn)
        Space: O(1)
        """
        return sum(sorted(nums)[::2])
