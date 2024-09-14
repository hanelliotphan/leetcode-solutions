class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        max_num = max(nums)
        longest = curr_len = 0

        for n in nums:
            if n == max_num:
                curr_len += 1
                longest = max(longest, curr_len)
            else:
                curr_len = 0
        
        return longest
