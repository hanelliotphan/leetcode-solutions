# https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        """
        Logic: Hash Map/Counter
        
        Time: O(n)
        Space: O(n)
        """
        counter = collections.Counter(nums)
        pairs = left = 0

        for k, v in counter.items():
            pairs += v // 2
            if v % 2 == 0:
                counter[k] = 0
            else:
                counter[k] = 1
                left += 1
            
        return [pairs, left]
