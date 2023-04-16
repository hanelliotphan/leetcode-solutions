# https://leetcode.com/problems/capitalize-the-title/description/

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        words = title.split()
        
        for i in range(len(words)):
            if len(words[i]) < 3:
                words[i] = words[i].lower()
            else:
                words[i] = words[i][0].upper() + words[i][1:].lower()
    
        return " ".join(words)
