# https://leetcode.com/problems/merge-strings-alternately/description/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        res = ""
        mn = min(len(word1), len(word2))
        mnw = word1 if len(word1) < len(word2) else word2

        for i in range(mn):
            res += (word1[i]+word2[i])
        
        if mnw == word1:
            res += word2[mn:]
        elif mnw == word2:
            res += word1[mn:]
        
        return res
