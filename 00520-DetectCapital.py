# https://leetcode.com/problems/detect-capital/description/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        first_upper = False
        mid_upper = False
        len_upper = 0
        
        for i in range(len(word)):
            if word[i].isupper():
                len_upper += 1
            if word[i].isupper() and i == 0:
                first_upper = True
            if word[i].isupper() and i != 0:
                mid_upper = True
                
        if len_upper == len(word) or len_upper == 0:
            return True
        if first_upper == True and mid_upper == False:
            return True
        
        return False
