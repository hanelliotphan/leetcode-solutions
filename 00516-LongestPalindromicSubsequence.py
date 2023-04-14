# https://leetcode.com/problems/longest-palindromic-subsequence/description/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        Logic: Dynamic Programming (Bottom-up)

        Time: O(n)
        Space: O(n)
        """
        n = len(s)
        dp = [0]*n

        for i in range(n-1, -1, -1):
            prev = 0
            for j in range(i, n):
                if i == j:
                    dp[j] = 1
                elif s[i] == s[j]:
                    prev, dp[j] = dp[j], 2 + prev
                else:
                    prev = dp[j]
                    dp[j] = max(dp[j], dp[j-1])
        
        return dp[-1]
