# https://leetcode.com/problems/next-greater-element-i/description/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Logic: Brute Force
        
        Time: O(n^2)
        Space: O(1)
        """
        res = []
        
        for n in nums1:
            flag = False
            idx = nums2.index(n)
            for m in nums2[idx+1:]:
                if m > n:
                    res.append(m)
                    flag = True
                    break
            if not flag:
                res.append(-1)
        
        return res
