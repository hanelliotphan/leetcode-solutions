# https://leetcode.com/problems/confusing-number/

class Solution:
    def confusingNumber(self, n: int) -> bool:
        """
        Logic: Brute Force
        
        Time: O(d)
        Space: O(d) -- d = number of digits of `n`
        """
        if n == 0: return False

        confusing_nums = {
            0: 0, 1: 1, 6: 9, 8: 8, 9: 6
        }
        n_copy = n
        digits = []

        while n_copy > 0:
            d = n_copy % 10
            if d not in confusing_nums:
                return False
            else:
                digits.append(str(confusing_nums[d]))
            n_copy //= 10

        return int("".join(digits)) != n
