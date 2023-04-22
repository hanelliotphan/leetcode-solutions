class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        """
        Logic: String slicing
        
        Time: O(n)
        Space: O(1)
        """
        max_num = float("-inf")

        for i, n in enumerate(number):
            if n == digit:
                max_num = max(max_num, int(number[:i]+number[i+1:]))
        
        return str(max_num)
