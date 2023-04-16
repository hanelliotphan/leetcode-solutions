# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        """
        Logic: Counting
        
        Time: O(n)
        Space: O(1)
        """
        max_score = -1

        for i in range(1, len(s)):
            print(s[:i])
            score = s[:i].count('0') + s[i:].count('1')
            max_score = max(max_score, score)
        
        return max_score
