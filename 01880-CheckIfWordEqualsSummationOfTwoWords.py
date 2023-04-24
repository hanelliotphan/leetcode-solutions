# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/description/

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        """
        Logic: Brute Force with ASCII
        
        Time: O(a+b+c)
        Space: O(a+b+c)
        """
        w1 = w2 = w3 = ""

        for ch in firstWord:
            w1 += str(ord(ch)-ord('a'))
        
        for ch in secondWord:
            w2 += str(ord(ch)-ord('a'))
        
        for ch in targetWord:
            w3 += str(ord(ch)-ord('a'))
        
        return int(w1) + int(w2) == int(w3)
