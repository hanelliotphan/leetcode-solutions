# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        pos = neg = 0

        for n in nums:
            if n < 0:
                neg += 1
            elif n > 0 :
                pos += 1

        return max(neg, pos)
