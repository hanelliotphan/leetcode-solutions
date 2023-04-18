# https://leetcode.com/problems/two-sum-less-than-k/description/

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        """
        Logic: Two Pointers with Sort
        
        Time: O(n*logn)
        Space: O(1)
        """
        nums.sort()
        curr_max = -1
        l = 0; r = len(nums)-1

        while l < r:
            total = nums[l] + nums[r]
            if total >= k:
                r -= 1
            elif total < k:
                curr_max = max(curr_max, total)
                l += 1
        
        return curr_max
