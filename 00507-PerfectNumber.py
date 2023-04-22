# https://leetcode.com/problems/perfect-number/description/

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        """
        Logic: Brute Force with Optimization
        
        Time: O(sqrt(n))
        Space: O(1)
        """
        if num <= 1:
            return False
        
        total = 0

        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                total += (i + num//i)
        
        return total+1 == num
