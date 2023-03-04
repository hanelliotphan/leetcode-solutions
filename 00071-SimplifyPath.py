# https://leetcode.com/problems/simplify-path/description/

class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Logic: Stack
        
        Time: O(n)
        Space: O(n)
        """
        stack = []
        
        for path_component in path.split("/"):
            if path_component == "..":
                if stack: stack.pop()
            elif path_component == "." or not path_component:
                continue
            else:
                stack.append(path_component)
                
        return "/" + "/".join(stack)
