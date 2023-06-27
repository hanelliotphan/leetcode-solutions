# https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Logic: Hash Map/Counter

        Time: O(n)
        Space: O(n)
        """
        num_count = collections.Counter(nums)
        
        for n in range(len(nums)+1):
            if not num_count[n]:
                return n
        
        return -1
