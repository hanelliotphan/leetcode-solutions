# https://leetcode.com/problems/validate-stack-sequences/description/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        Logic: Stack

        Time: O(n)
        Space: O(n)
        """
        stack = []
        i = 0

        for n in pushed:
            stack.append(n)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        
        return i == len(popped)
