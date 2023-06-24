class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Logic: Sliding Window

        Time: O(n)
        Space: O(1)
        """
        if k <= 1:
            return 0

        i = res = 0
        curr_window = 1

        for j in range(len(nums)):
            curr_window *= nums[j]
            while curr_window >= k:
                curr_window //= (nums[i])
                i += 1
            res += (j-i+1)

        return res 
