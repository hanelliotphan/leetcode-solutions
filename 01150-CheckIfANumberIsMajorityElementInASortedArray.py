class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        """
        Logic: Hash Map/Counter
        
        Time: O(n)
        Space: O(n)
        """
        counter = collections.Counter(nums)

        return counter[target] > len(nums) // 2 if target in counter else False
