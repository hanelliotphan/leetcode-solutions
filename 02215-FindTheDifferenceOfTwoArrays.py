# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        Logic: Hash Set
        
        Time: O(n)
        Space: O(1)
        """
        return [list(set(nums1)-set(nums2)), list(set(nums2)-set(nums1))]
