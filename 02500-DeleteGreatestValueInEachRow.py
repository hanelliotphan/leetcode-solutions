# https://leetcode.com/problems/delete-greatest-value-in-each-row/description/

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        """
        Logic: Brute Force

        Time: O(m*n)
        Space: O(1)
        """
        max_val = 0

        for row in grid:
            row.sort()

        # Replace the max value of row with float("-inf")
        # and increment the max_val
        for j in range(len(grid[0])):
            row_max = float("-inf")
            for row in grid:
                row_max = max(row_max, row[j])
            max_val += row_max

        return max_val
            
