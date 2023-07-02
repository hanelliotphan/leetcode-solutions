# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        """
        Logic: Brute Force with Sort

        Time: O(n*logn)
        Space: O(1)
        """
        for _ in range(k):
            mn = min(nums)
            nums.remove(mn)
            nums.append(-mn)
        
        return sum(nums)
