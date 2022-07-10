class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Logic: Hashmap
        
        Time: O(n)
        Space: O(n)
        """
        hash_map = {} # key=num, val=index
        res = []
        
        for i in range(len(nums)):
            hash_map[nums[i]] = i
            
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in hash_map and hash_map[remainder] != i:
                return [i, hash_map[remainder]]
            
        return []
