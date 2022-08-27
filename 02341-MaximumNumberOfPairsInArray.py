class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        """
        Logic: Hash Set / Counter / Divmod
        
        Time: O(n)
        Space: O(n)
        """
        if len(nums) == 1: 
            return [0, 1]
        
        counter = collections.Counter(nums)
        pairs = rem = 0
        
        for freq in counter.values():
            pairs += freq // 2
            rem += divmod(freq, 2)[1]
            
        return [pairs, rem]
            
