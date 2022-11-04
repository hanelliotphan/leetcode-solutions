# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Logic: Stack of vowels
        
        Time: O(n)
        Space: O(n)
        """
        vowels = []
        
        for c in s:
            if c in "aeiou" or c in "AEIOU":
                vowels.append(c)
        
        new_word = ""
        for c in s:
            if c not in "aeiou" and c not in "AEIOU":
                new_word += c
            else:
                new_word += vowels[-1]
                vowels.pop()
        
        return new_word
