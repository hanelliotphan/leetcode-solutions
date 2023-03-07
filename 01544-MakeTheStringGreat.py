# https://leetcode.com/problems/make-the-string-great/description/

class Solution:
    def makeGood(self, s: str) -> str:
        """
        Logic: Stack
        
        Time: O(n)
        Space: O(n)
        """
        stack = []
        
        for ch in s:
            if stack and abs(ord(ch)-ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(ch)
                
        return "".join(stack)
