class Solution:
    def maxDepth(self, s: str) -> int:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        res = curr = 0

        for ch in s:
            if ch == "(":
                curr += 1
                res = max(res, curr)
            elif ch == ")":
                curr -= 1
        
        return res
