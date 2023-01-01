# https://leetcode.com/problems/count-the-digits-that-divide-a-number/

class Solution:
    def countDigits(self, num: int) -> int:
        """
        Logic: Brute Force
        
        Time: O(digits) / O(1)
        Space: O(1)
        """
        count = 0
        n = num
        
        while n > 0:
            digit = divmod(n, 10)[1]
            if num % digit == 0:
                count += 1
            n //= 10
            
        return count
