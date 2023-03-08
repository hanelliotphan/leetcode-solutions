# https://leetcode.com/problems/count-distinct-numbers-on-board/description/

class Solution:
    def distinctIntegers(self, n: int) -> int:
        """
        Logic: Mathematical approach

        Time: O(1)
        Space: O(1)
        """
        return 1 if n == 1 else n-1
