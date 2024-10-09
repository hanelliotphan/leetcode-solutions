class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        Logic: One Pass

        Time: O(n)
        Space: O(1)
        """
        open = close = 0

        for ch in s:
            if ch == "(":
                open += 1
                continue
            elif open:
                open -= 1
            else:
                close += 1
        
        return open + close
