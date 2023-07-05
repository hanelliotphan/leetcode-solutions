# https://leetcode.com/problems/max-consecutive-ones-iii/description/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Logic: Sliding Window

        Time: O(n)
        Space: O(1)
        """
        start = 0
        n = len(nums)
        
        for curr in range(n):
            k -= (1-nums[curr])
            if k < 0:
                k += (1-nums[start])
                start += 1
        
        return curr-start+1
