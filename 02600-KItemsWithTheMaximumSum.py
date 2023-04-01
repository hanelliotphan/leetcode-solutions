# https://leetcode.com/problems/k-items-with-the-maximum-sum/description/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        max_sum = 0

        while k > 0:
            if numOnes > 0:
                max_sum += 1
                numOnes -= 1
            elif numZeros > 0:
                max_sum += 0
                numZeros -= 1
            elif numNegOnes > 0:
                max_sum -= 1
                numNegOnes -= 1
            k -= 1

        return max_sum
