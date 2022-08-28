class Solution:
    def largestInteger(self, num: int) -> int:
        """
        Logic: Brute Force with Sort
        
        Time: O(n*logn)
        Space: O(n)
        """
        digits = []
        even_digits = []
        odd_digits = []
        n = num
        
        while n > 0:
            d = n % 10
            if d % 2 == 0:
                even_digits.append(d)
            else:
                odd_digits.append(d)
            digits.append(d)
            n //= 10
            
        digits = digits[::-1]
        even_digits.sort()
        odd_digits.sort()
        
        for i in range(len(digits)):
            if digits[i] % 2 == 0:
                digits[i] = even_digits[-1]
                even_digits.pop()
            else:
                digits[i] = odd_digits[-1]
                odd_digits.pop()
                
        res = 0
        for i in range(1, len(digits)+1):
            res += digits[-i] * pow(10, i-1)
        
        return res
