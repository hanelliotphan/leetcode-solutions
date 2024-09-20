class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        Logic: Brute Force

        Time: O(n^2)
        Space: O(n)
        """
        n = len(s)

        for i in range(n):
            if s[:n-i] == s[::-1][i:]:
                return s[::-1][:i] + s
        
        return ""
