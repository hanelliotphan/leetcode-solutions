class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        """
        Logic: Hash Map
        
        Time: O(n)
        Space: O(n)
        """
        counter = collections.Counter(nums)
        count = 0
        
        for n in nums:
            if n + k in nums:
                count += counter[n+k]
        
        return count
