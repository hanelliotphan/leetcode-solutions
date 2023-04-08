# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        """
        Logic: Hash Map

        Time: O(n * max(counter.values()))
        Space: O(n)
        """
        counter = collections.Counter(nums)
        res = [[0] for _ in range(max(list(counter.values())))]

        for i in range(len(nums)):
            j = 0
            while counter[nums[i]] > 0:
                res[j].append(nums[i])
                j += 1
                counter[nums[i]] -= 1
        
        return [r[1:] for r in res]
