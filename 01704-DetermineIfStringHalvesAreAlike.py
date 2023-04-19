# https://leetcode.com/problems/determine-if-string-halves-are-alike/description/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        mid = len(s) // 2
        c1 = c2 = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        for ch in s[:mid]:
            if ch in vowels: c1 += 1

        for ch in s[mid:]:
            if ch in vowels: c2 += 1
        
        return c1 == c2
