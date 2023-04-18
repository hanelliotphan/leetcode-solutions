# https://leetcode.com/problems/delete-columns-to-make-sorted/description/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        Logic: Brute Force with ASCII
        
        Time: O(n*m)
        Space: O(1)
        """
        r = len(strs)
        c = len(strs[0])
        count = 0

        for j in range(c):
            for i in range(1, r):
                if ord(strs[i][j]) < ord(strs[i-1][j]):
                    count += 1
                    break
        
        return count
