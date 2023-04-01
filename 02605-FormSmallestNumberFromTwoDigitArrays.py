# https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/description/

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Logic: Brute Force

        Time: O(1)
        Space: O(min(m, n))
        """
        if set(nums1) & set(nums2):
            return min(set(nums1) & set(nums2))
        
        return min(min(nums1)*10 + min(nums2), min(nums2)*10 + min(nums1))
