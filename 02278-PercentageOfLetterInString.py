class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        """
        Logic: Straightforward
        
        Time: O(n)
        Space: O(1)
        """
        n = len(s)
        count = 0
        
        for ch in s:
            if ch == letter:
                count += 1
        
        return count*100 // n
