# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        count = 0

        for i in range(len(s)-2):
            if s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2]:
                count += 1
        
        return count
