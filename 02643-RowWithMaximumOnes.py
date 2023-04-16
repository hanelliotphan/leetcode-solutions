# https://leetcode.com/problems/row-with-maximum-ones/description/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        curr_min_idx = -1
        curr_max_count = 0

        for i in range(len(mat)):
            count = mat[i].count(1)
            if count > curr_max_count:
                curr_max_count = count
                curr_min_idx = i
                
        
        return [curr_min_idx, curr_max_count] if curr_min_idx != -1 else [0, 0]
