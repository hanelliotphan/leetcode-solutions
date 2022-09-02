# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

class Solution:
    def greatestLetter(self, s: str) -> str:
        """
        Logic: ASCII Ord/Chr
        
        Time: O(n)
        Space: O(1)
        """
        max_dups = -1
        
        for ch in s:
            if ch.islower() and chr(ord(ch)-32) in s:
                max_dups = max(max_dups, ord(ch.upper()))
            elif ch.isupper() and chr(ord(ch)+32) in s:
                max_dups = max(max_dups, ord(ch))
                
        return chr(max_dups) if max_dups != -1 else ""
