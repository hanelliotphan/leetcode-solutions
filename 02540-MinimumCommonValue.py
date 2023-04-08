# https://leetcode.com/problems/minimum-common-value/description/

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        common_values = set(set(nums1) & set(nums2))
        return min(common_values) if common_values else -1
