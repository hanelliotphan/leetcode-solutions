# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Logic: Dynamic Programming (Bottom-Up with Memoization)
            Start from the second last row and from the second last column,
            compute the possible ways to reach the destination.
            Then return the first value of the first row
        
        Time: O(n*m)
        Space: O(n)
        """
        row = [1]*n
        
        for i in range(m-1):
            new_row = [1]*n
            for j in range(n-2, -1, -1):
                new_row[j] = row[j] + new_row[j+1]
            row = new_row
            
        return row[0]
