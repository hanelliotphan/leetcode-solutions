# https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/description/

class Solution:
    def countLetters(self, s: str) -> int:
        """
        Logic: Dynamic Programming
        
        Time: O(n)
        Space: O(1)
        """
        curr_total = total = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr_total += 1
            else:
                curr_total = 1
            total += curr_total

        return total
