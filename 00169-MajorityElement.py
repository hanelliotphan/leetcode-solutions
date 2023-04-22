class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(n)
        """
        counter = collections.Counter(nums)

        for k, v in counter.items():
            if v > len(nums) / 2:
                return k
        
        return -1
