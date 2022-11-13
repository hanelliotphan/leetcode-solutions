class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        """
        Logic: Hash Set
        
        Time: O(n*logn)
        Space: O(n)
        """
        nums = sorted(nums)
        averages = set()
        
        while len(nums) > 0:
            avg = (nums.pop(0) + nums.pop(-1)) / 2
            averages.add(avg)
            
        return len(averages)
