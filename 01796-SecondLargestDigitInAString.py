class Solution:
    def secondHighest(self, s: str) -> int:
        """
        Logic: Straightforward
        
        Time: O(n)
        Space: O(1)
        """
        largest = second_largest = -1
        
        for ch in s:
            if 48 <= ord(ch) <= 57:
                digit = ord(ch) - ord('0')
                if largest < digit:
                    second_largest = largest
                    largest = digit
                elif second_largest < digit and digit < largest:
                    second_largest = digit
                    
        return second_largest
