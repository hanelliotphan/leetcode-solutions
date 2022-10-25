# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        Logic: Straightforward Concatenation
        
        Time: O(m + n)
        Space: O(1)
        """
        w1 = ""
        w2 = ""
        
        for w in word1:
            w1 += w
            
        for w in word2:
            w2 += w
            
        return w1 == w2
