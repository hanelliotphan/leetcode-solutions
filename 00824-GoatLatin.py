class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        """
        Logic: Brute Force
        
        Time: O(w)
        Space: O(w)
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        words = sentence.split()
        
        for i in range(len(words)):
            if words[i][0] not in vowels:
                new_word = words[i][1:] + words[i][0]
                words[i] = new_word
            words[i] += "ma"
            words[i] += "a"*(i+1)
            
        return " ".join(words)
