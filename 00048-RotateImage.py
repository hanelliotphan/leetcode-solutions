class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Logic: Swap cell by cell, then reverse each row by column
        
        Time: O(n^2)
        Space: O(1)
        """
        rows = len(matrix)
        
        for r in range(rows):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                
        for i in range(rows):
            matrix[i] = matrix[i][::-1]
