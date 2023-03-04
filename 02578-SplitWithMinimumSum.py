# https://leetcode.com/problems/split-with-minimum-sum/description/

class Solution:
    def splitNum(self, num: int) -> int:
        """
        Logic: Sorting Digits

        Time: O(1) --> since the maximum num has only 10 digits
        Space: O(1) --> since the maximum num has only 10 digits
        """
        n = num
        digits = []

        while n > 0:
            d = n % 10
            digits.append(d)
            n //= 10

        digits = sorted(digits)

        return int(''.join([str(i) for i in digits[::2]])) + int(''.join([str(i) for i in digits[1::2]]))
