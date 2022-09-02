class Solution:
    def maximum69Number (self, num: int) -> int:
        """
        Logic: Brute Force
        
        Time: O(d) -- d = digits in `num`
        Space: O(d)
        """
        digits = []
        
        while num > 0:
            digits.append(num % 10)
            num //= 10
            
        digits = digits[::-1]
        
        for i in range(len(digits)):
            if digits[i] == 6:
                digits[i] = 9
                break
                
        return int("".join(str(i) for i in digits))
