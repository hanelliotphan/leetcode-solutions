class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        """
        Logic: Index
        
        Time: O(n) -- n = len(word)
        Space: O(1)
        """
        curr_pos = res = 0
        
        for ch in word:
            idx = keyboard.index(ch)
            res += (abs(idx-curr_pos))
            curr_pos = idx
            
        return res
