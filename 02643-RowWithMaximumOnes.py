# https://leetcode.com/problems/row-with-maximum-ones/description/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        curr_max_count = float("-inf")
        curr_idx = float("inf")

        for i in range(len(mat)):
            one_count = mat[i].count(1)
            if one_count > curr_max_count:
                curr_max_count = one_count
                curr_idx = i
        
        return [curr_idx, curr_max_count]
