# https://leetcode.com/problems/build-array-from-permutation/description/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        return [nums[nums[i]] for i in range(len(nums))]
