# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        Logic: Two Pointers
        
        Time: O(m+n)
        Space: O(1)
        """
        count = 0
        i = len(grid)-1; j = 0

        while i >= 0 and j < len(grid[0]):
            if grid[i][j] < 0:
                count += len(grid[0])-j
                i -= 1
            else:
                j += 1
        
        return count
