# https://leetcode.com/problems/excel-sheet-column-number/description/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        res = 0
        n = len(columnTitle)

        for i in range(n):
            res *= 26
            res += ord(columnTitle[i])-ord('A')+1

        return res
