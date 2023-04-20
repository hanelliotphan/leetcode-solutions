# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/

class Solution:
    def minimumSum(self, num: int) -> int:
        """
        Logic: Brute Force with Sort
        
        Time: O(d*logd)
        Space: O(d)
        """
        digits = []

        while num > 0:
            digits.append(num % 10)
            num //= 10
        
        digits = sorted(digits)

        return digits[0]*10+digits[2] + digits[1]*10+digits[3]
