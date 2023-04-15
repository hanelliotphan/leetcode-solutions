# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/description/

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        """
        Logic: Brute Force
        
        Time: O(n^2)
        Space O(n)
        """
        n = len(matrix)

        for r in range(n):
            rs = set()
            cs = set()
            for c in range(n):
                rs.add(matrix[r][c])
                cs.add(matrix[c][r])
            if len(rs) < n or len(cs) < n:
                return False
        
        return True
