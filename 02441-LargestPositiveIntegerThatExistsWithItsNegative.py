# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        max_n = float("-inf")

        for n in nums:
            if (n * -1) in nums:
                max_n = max(abs(n), max_n)

        return max_n if max_n > 0 else -1
