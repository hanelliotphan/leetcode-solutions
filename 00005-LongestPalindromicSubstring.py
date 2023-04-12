# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Logic: String expansion

        Time: O(n^2)
        Space: O(1)
        """
        n = len(s)
        res = ""

        def expand(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i, j = i-1, j+1
            return s[i+1:j]
        
        for i in range(n):
            res = max(res, expand(i,i), expand(i,i+1), key=len)
        
        return res
