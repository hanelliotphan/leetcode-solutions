# https://leetcode.com/problems/sum-of-unique-elements/description/

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        """
        Logic: Hash Map/Counter
        
        Time: O(n)
        Space: O(n)
        """
        total = 0
        counter = collections.Counter(nums)

        for k, v in counter.items():
            if v == 1:
                total += k
        
        return total
