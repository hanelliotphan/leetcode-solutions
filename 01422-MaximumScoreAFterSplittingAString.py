# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        """
        Logic: Counting
        
        Time: O(n)
        Space: O(1)
        """
        max_score = 0
        
        for i in range(1, len(s)):
            left = s[:i].count("0")
            right = s[i:].count("1")
            max_score = max(max_score, left + right)
            
        return max_score
