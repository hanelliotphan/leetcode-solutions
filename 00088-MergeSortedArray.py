# https://leetcode.com/problems/merge-sorted-array/description/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        Logic: Brute Force

        Time: O(n*log(m+n))
        Space: O(1)
        """
        for i in range(n):
            nums1[i+m] = nums2[i]
        
        return nums1.sort()
