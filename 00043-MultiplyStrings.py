# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Logic: Have a helper to change from current string number
                to integer, then multiply the two numbers together 
                and convert to strings
        
        Time: O(m+n)
        Space: O(1)
        """   
        def get_int(num):
            mult = 1
            res = 0
            for digit in reversed(num):
                res += (ord(digit)-ord('0')) * mult
                mult *= 10
            return res
        
        return str(get_int(num1) * get_int(num2))
