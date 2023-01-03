# https://leetcode.com/problems/delete-columns-to-make-sorted/description/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        Logic: ASCII 

        Time: O(n^2)
        Space: O(1)
        """
        r, c = len(strs), len(strs[0])
        num_cols_to_delete = 0

        for j in range(c):
            for i in range(1, r):
                if ord(strs[i][j]) < ord(strs[i-1][j]):
                    num_cols_to_delete += 1
                    break
        
        return num_cols_to_delete
