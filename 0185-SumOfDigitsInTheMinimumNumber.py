# https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/description/

class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        """
        Logic: Brute Force
        
        Time: O(log10(n))
        Space: O(1)
        """
        min_num = min(nums)
        res = 0

        while min_num > 0:
            res += min_num % 10
            min_num //= 10
        
        return 0 if res % 2 else 1
