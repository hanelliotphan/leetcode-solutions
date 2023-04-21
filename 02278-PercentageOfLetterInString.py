# https://leetcode.com/problems/percentage-of-letter-in-string/description/

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        """
        Logic: Brute Force with Count (1-liner)
        
        Time: O(n)
        Space: O(1)
        """
        return floor(s.count(letter)/len(s) * 100)
