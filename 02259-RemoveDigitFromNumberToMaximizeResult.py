class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        """
        Logic: String slicing
        
        Time: O(n)
        Space: O(1)
        """
        res = 0
        
        for i, d in enumerate(list(number)):
            if d == digit:
                res = max(res, int(number[:i] + number[i+1:]))
                
        return str(res)
