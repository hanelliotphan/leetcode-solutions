# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Logic: Stack

        Time: O(n)
        Space: O(m)
        """
        stack = []
        closes = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in closes.values():
                stack.append(ch)
            elif stack and closes[ch] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return True
