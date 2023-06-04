# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Logic: Brute Force (String Reverse Loop)
        
        Time: O(n)
        Space: O(1)
        """
        i = len(s)
        l = 0

        while i > 0:
            i -= 1
            if s[i] != " ": l += 1
            else:
                if l > 0: return l
        
        return l
