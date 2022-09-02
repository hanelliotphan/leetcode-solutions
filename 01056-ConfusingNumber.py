# https://leetcode.com/problems/confusing-number/

class Solution:
    def confusingNumber(self, n: int) -> bool:
        """
        Logic: Brute Force
        
        Time: O(d)
        Space: O(d) -- d = number of digits of `n`
        """
        confusing_digits = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6
        }
        
        digits = []
        tmp = n
        new_n = ""
        
        if n == 0 or n == 1 or n == 8:
            return False
        elif n == 6 or n == 9:
            return True
        
        while tmp > 0:
            d = tmp % 10
            if d not in confusing_digits.keys():
                return False
            digits.append(d)
            new_n += str(confusing_digits[d])
            tmp //= 10
            
        if len(set(digits)) == 1:
            return False
        
        if int(new_n) == n:
            return False
                
        return True
