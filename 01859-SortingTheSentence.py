# https://leetcode.com/problems/sorting-the-sentence/description/

class Solution:
    def sortSentence(self, s: str) -> str:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(n)
        """
        res = [""] * len(s)
        words = s.split()

        for word in words:
            res[int(word[-1])-1] = word[:-1]
        
        return " ".join(res).strip()
