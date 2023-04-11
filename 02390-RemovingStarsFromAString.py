# https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:
        """
        Logic: Stack

        Time: O(n)
        Space: O(n)
        """
        stack = []
        
        for ch in s:
            if ch != "*":
                stack.append(ch)
            else:
                stack.pop(-1)
        
        return "".join(stack)
