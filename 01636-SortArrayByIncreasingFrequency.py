class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        Logic: Hash Map/Counter with Sort
        
        Time: O(n*logn)
        Space: O(n)
        """
        freqs = collections.Counter(nums)
        
        return sorted(nums, key=lambda x: (freqs[x], -x))
