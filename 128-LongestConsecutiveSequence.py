class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Logic: Hash Set with keeping track of 
            current steakand longest streak
        
        Time: O(n)
        Space: O(n)
        """
        longest_streak = 0
        num_set = set(nums)
        
        for num in nums:
            if num-1 not in num_set:
                curr_num = num
                curr_streak = 1
                
                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_streak += 1
                
                longest_streak = max(longest_streak, curr_streak)
        
        return longest_streak
