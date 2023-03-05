# https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        """
        Logic: Mathematical approach

        Time: O(1)
        Space: O(1)
        """
        return n - abs(n-1 - time % (2*n-2))
