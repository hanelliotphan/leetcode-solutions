# https://leetcode.com/problems/armstrong-number/description/

class Solution:
    def isArmstrong(self, n: int) -> bool:
        """
        Logic: Brute Force with Log10
        
        Time: O(d) --> number of digits in `n`
        Space: O(1)
        """
        n_copy = n
        total = 0
        l = int(math.log10(n))+1

        while n_copy > 0:
            total += (n_copy%10)**l
            n_copy //= 10
        
        return total == n
