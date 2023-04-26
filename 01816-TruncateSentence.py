class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        res = ""

        for ch in s:
            if ch == " ": k -= 1
            if k == 0: break
            res += ch
        
        return res
