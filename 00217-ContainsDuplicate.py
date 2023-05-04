# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Logic: Hash Map/Counter
        
        Timne: O(n)
        Space: O(n)
        """
        counter = collections.Counter(nums)

        for k, v in counter.items():
            if v > 1:
                return True

        return False
