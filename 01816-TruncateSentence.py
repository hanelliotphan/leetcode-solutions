class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        """
        Logic: One pointer
        
        Time: O(n) -- n == number of characters in `s`
        Space: O(1)
        """
        words_met = 0
        
        for i, c in enumerate(s):
            if c == " ":
                words_met += 1
                if words_met == k:
                    return s[:i]
        
        return s
