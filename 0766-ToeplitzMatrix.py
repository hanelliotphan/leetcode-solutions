# https://leetcode.com/problems/toeplitz-matrix/description/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        Logic: Brute Force:
        
        Time: O(m*n)
        Space: O(1)
        """
        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if not (r == 0 or c == 0 or matrix[r-1][c-1] == cell):
                    return False
        
        return True
