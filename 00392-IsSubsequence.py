class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Logic: Two pointer
            Compute how many characters in `s` also exist in `t`.
            Return true if all characters in `s` exist in `t`t
        
        Time: O(n)
        Space: O(1)
        """
        l, r = 0, 0
        
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1
            r += 1
            
        return l == len(s)
