# https://leetcode.com/problems/left-and-right-sum-differences/description/

class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        """
        Logic: Brute Force

        Time: O(n^2) --> sum() takes O(n) time
        Space: O(1) --> need to return an `O(n) array`, no extra data is needed
        """
        res = []

        for i in range(len(nums)):
            if i == 0:
                res.append(sum(nums[i+1:]))
            elif i == len(nums)-1:
                res.append(sum(nums[:i]))
            else:
                res.append(abs(sum(nums[:i])-sum(nums[i+1:])))

        return res
