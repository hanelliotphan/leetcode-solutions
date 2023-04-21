# https://leetcode.com/problems/largest-unique-number/description/

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        """
        Logic: Hash Map/Counter
        
        Time: O(n)
        Space: O(n)
        """
        counter = collections.Counter(nums)
        max_unique = -1

        for k, v in counter.items():
            if v == 1:
                max_unique = max(max_unique, k)
        
        return max_unique
