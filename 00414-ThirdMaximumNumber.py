# https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        Logic: Hash Set
        
        Time: O(n)
        Space: O(n)
        """
        max_nums = set()

        for n in nums:
            max_nums.add(n)
            if len(max_nums) > 3:
                max_nums.remove(min(max_nums))
        
        if len(max_nums) == 3:
            return min(max_nums)
        
        return max(max_nums)
