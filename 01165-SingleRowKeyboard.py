# https://leetcode.com/problems/single-row-keyboard/description/

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        """
        Logic: Hash Map
        
        Time: O(w)
        Space: O(26) --> O(1)
        """
        indices = {k: v for v, k in enumerate(keyboard)}
        curr_pos = time = 0

        for ch in word:
            time += abs(indices[ch]-curr_pos)
            curr_pos = indices[ch]
        
        return time
