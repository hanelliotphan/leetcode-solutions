# https://leetcode.com/problems/left-and-right-sum-differences/description/

class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        """
        Logic: Prefix Sum
        
        Time: O(n)
        Space: O(n)
        """
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        res = []

        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        for i in range(len(nums)):
            if i == 0:
                res.append(abs(0-prefix_sum[i-1]+prefix_sum[i]))
            elif i == len(nums)-1:
                res.append(abs(prefix_sum[i-1]))
            else:
                res.append(abs(prefix_sum[i-1]-abs(prefix_sum[i]-prefix_sum[-1])))

        return res
