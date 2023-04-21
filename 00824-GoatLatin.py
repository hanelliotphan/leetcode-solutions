# https://leetcode.com/problems/goat-latin/description/

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(n)
        """
        words = sentence.split()
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        for i, word in enumerate(words):
            if word in vowels:
                words[i] += ("ma" + "a"*(i+1))
            elif word[0] not in vowels:
                words[i] = (word[1:]+word[0]+"ma"+"a"*(i+1))
            else:
                words[i] = word+"ma"+"a"*(i+1)
        
        return " ".join(words)
