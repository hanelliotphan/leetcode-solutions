# https://leetcode.com/problems/simplify-path/description/

class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Logic: Stack

        Time: O(n)
        Space: O(n)
        """
        path_components = path.split("/")
        stack = []

        for comp in path_components:
            if not comp or comp == ".":
                continue
            elif comp == "..":
                if stack: stack.pop()
            else:
                stack.append(comp)
        
        return "/" + "/".join(stack)
