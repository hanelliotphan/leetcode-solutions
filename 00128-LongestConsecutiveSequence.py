class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Logic: Hash set interation

        Time: O(n)
        Space: O(n)
        """
        hash_set = set(nums)
        longest = 0

        for n in nums:
            curr_longest = m = 0
            if n-1 not in hash_set:
                m = n
                curr_longest = 1
                while m+1 in hash_set:
                    m += 1
                    curr_longest += 1
                longest = max(longest, curr_longest)
        
        return longest
