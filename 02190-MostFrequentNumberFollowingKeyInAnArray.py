class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        """
        Logic: Hash Map/Counter
        
        Time: O(n)
        Space: O(n)
        """
        target = collections.defaultdict(int)

        for i in range(len(nums)-1):
            if nums[i] == key:
                target[nums[i+1]] += 1
        
        for k, v in target.items():
            if v == max(target.values()):
                return k
        
        return max(target.values())
