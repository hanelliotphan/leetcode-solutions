# https://leetcode.com/problems/largest-unique-number/description/

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        """
        Logic: Hash Map/Counter
        
        Time: O(n)
        Space: O(n)
        """
        counter = collections.Counter(nums)
        largest = float("-inf")
        
        for k, v in counter.items():
            if k > largest and v == 1:
                largest = k
        
        return largest if largest != float("-inf") else -1
