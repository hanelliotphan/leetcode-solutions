# https://leetcode.com/problems/perform-string-shifts/description/

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        """
        Logic: Get net left shift
        
        Time: O(shift)
        Space: O(1)
        """
        total_l = 0

        for d, a in shift:
            if d == 1: a = -a
            total_l += a
        
        total_l %= len(s)
        s = s[total_l:] + s[:total_l]

        return s
