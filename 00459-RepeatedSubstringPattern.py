# https://leetcode.com/problems/repeated-substring-pattern/description/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        for i in range(1, len(s)//2+1):
            w = len(s) // i
            if len(s) % i == 0 and s[:i]*w == s:
                return True
        
        return False
