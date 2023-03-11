# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Logic: Brute Force

        Time: O(m*n)
        Space: O(1)
        """
        m, n = len(matrix), len(matrix[0])

        zero_in_first_row = any(matrix[0][c] == 0 for c in range(n))
        zero_in_first_col = any(matrix[r][0] == 0 for r in range(m))

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[0][c] = matrix[r][0] = 0

        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if zero_in_first_row:
            for c in range(n):
                matrix[0][c] = 0
        
        if zero_in_first_col:
            for r in range(m):
                matrix[r][0] = 0
