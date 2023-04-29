# https://leetcode.com/problems/long-pressed-name/description/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        """
        Logic: Two Pointers
        
        Time: O(t)
        Space: O(1)
        """
        i = 0

        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j-1]:
                return False

        return i == len(name)
