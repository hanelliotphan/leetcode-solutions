# https://leetcode.com/problems/count-integers-with-even-digit-sum/description/

class Solution:
    def countEven(self, num: int) -> int:
        """
        Logic: Brute Force
        
        Time: O(n*logn)
        Space: O(1)
        """
        if num < 2:
            return 0
        
        count = 0
        i = 2
        
        while i <= num:
            j = i
            digit_sum = 0
            while j > 0:
                digit_sum += (j % 10)
                j //= 10
            if digit_sum % 2 == 0:
                count += 1
            i += 1
                
        return count
