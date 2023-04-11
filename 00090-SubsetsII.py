# https://leetcode.com/problems/subsets-ii/description/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Logic: Backtracking

        Time: O(n*2^n)
        Space: O(n)
        """
        def backtrack(start, curr, res):
            res.append(curr[::])
            for i in range(start, len(nums)):
                if i != start and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                backtrack(i+1, curr, res)
                curr.pop()
        
        nums.sort()
        res = []
        backtrack(0, [], res)

        return res
