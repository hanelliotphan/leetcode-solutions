# https://leetcode.com/problems/detect-capital/description/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        c1, c2, c3 = False, False, False

        if word == word.upper():
            c1 = True
        if word == word.lower():
            c2 = True
        if word[0] == word[0].upper() and word[1:] == word[1:].lower():
            c3 = True

        return c1 or c2 or c3
