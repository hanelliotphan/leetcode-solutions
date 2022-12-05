# https://leetcode.com/problems/circular-sentence/

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        n = len(sentence)
        i = 0
        is_match = True
        
        while i < n:
            if sentence[i] == " ":
                if sentence[i+1] != sentence[i-1]:
                    return False
            i += 1
                    
        return sentence[-1] == sentence[0]
