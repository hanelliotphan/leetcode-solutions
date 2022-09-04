# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        longest_sub = 1
        curr_longest = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_longest += 1
            else:
                curr_longest = 1
            longest_sub = max(longest_sub, curr_longest)
            
        return longest_sub
