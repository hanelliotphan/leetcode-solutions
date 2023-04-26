# https://leetcode.com/problems/strobogrammatic-number/description/

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        hm = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }
        flipped = ""

        for ch in num:
            if ch not in hm: return False
            flipped = hm[ch]+flipped
        
        return num == flipped
