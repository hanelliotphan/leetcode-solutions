# https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(max(range(1, 5)) --> O(1)
        """
        res = []

        for n in nums:
            digits = []
            while n > 0:
                digits.append(n % 10)
                n //= 10
            res.extend(digits[::-1])

        return res
