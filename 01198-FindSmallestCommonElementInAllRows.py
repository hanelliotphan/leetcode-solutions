# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/description

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        """
        Logic: Intersection of Set
        
        Time: O(m)
        Space: O(n)
        """
        s = set(mat[0])

        for m in mat:
            s = set(s) & set(m)
        
        return min(s) if len(s) > 0 else -1
