# https://leetcode.com/problems/number-of-good-pairs/description/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        Logic: Hash Map with Mathematical Approach
        
        Time: O(n)
        Space: O(n)
        """
        indices = collections.defaultdict(list)

        for i in range(len(nums)):
            indices[nums[i]].append(i)

        count = 0
        
        for k, v in indices.items():
            n = len(v)
            if n > 1:
                count += (n*(n-1)//2)
        
        return count
