# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        arr_sum = sum(nums)
        digit_sum = 0

        for n in nums:
            while n > 0:
                digit_sum += n % 10
                n //= 10

        return abs(arr_sum - digit_sum)
