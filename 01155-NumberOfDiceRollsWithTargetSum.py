# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        """
        Logic: Dynamic Programming (Bottom-Up)
        
        Time: O(d*f*target)
        Space: O(target)
        """
        dp = [0] * (target+1)
        dp[0] = 1
        MOD = 10**9+7
        
        for i in range(1, d+1):
            new_dp = [0] * (target+1)
            for j in range(1, f+1):
                for k in range(j, target+1):
                    new_dp[k] = (new_dp[k] + dp[k-j]) % MOD
            new_dp, dp = dp, new_dp
            
        return dp[target]
