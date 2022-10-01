# https://leetcode.com/problems/get-maximum-in-generated-array/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(n)
        """
        if n < 1:
            return 0
        if n <= 2:
            return 1
        
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(1, n//2+1):
            if 2 <= 2*i <= n:
                dp[2*i] = dp[i]
            if 2 <= 2*i+1 <= n:
                dp[2*i+1] = dp[i] + dp[i+1]
        
        return max(dp)
