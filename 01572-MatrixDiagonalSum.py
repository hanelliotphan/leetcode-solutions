# https://leetcode.com/problems/matrix-diagonal-sum/description/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        Logic: Brute Force
        
        Time: O(n) --> n = number of rows
        Space: O(1)
        """
        total = 0
        mid = len(mat) // 2

        for i in range(len(mat)):
            total += mat[i][i]
            total += mat[len(mat)-1-i][i]
        
        if len(mat) % 2:
            total -= mat[mid][mid]

        return total
