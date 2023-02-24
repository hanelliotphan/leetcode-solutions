# https://leetcode.com/problems/find-the-array-concatenation-value/description/

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        res = 0 if len(nums) % 2 == 0 else nums[len(nums)//2]

        for i in range(len(nums)//2):
            res += int(str(nums[i]) + str(nums[len(nums)-1-i]))

        return res
