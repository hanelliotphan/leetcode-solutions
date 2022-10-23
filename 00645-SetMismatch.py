# https://leetcode.com/problems/set-mismatch/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        Logic: Hash Map
        
        Time: O(n)
        Space: O(n)
        """
        desired = list(range(1, len(nums)+1))
        counter = collections.Counter(nums)
        dup = missing = float("inf")
        
        for k, v in counter.items():
            if v > 1:
                dup = k
                break
        
        for n in desired:
            if n not in nums:
                missing = n
                break
                
        return [dup, missing]
