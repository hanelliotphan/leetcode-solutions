# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """
        Logic: Using startswith()
        
        Time: O(n)
        Space: O(1)
        """
        words = sentence.split()
        
        for i in range(len(words)):
            if words[i].startswith(searchWord):
                return i+1
            
        return -1
