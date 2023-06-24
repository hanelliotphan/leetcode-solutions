# https://leetcode.com/problems/squares-of-a-sorted-array/description/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Logic: Two pointers (backwards)

        Time: O(n)
        Space: O(n)
        """
        n = len(nums)
        i = 0
        j = n-1
        res = [0]*n
        
        for k in range(n-1, -1, -1):
            if abs(nums[i]) < abs(nums[j]):
                square = nums[j]
                j -= 1
            else:
                square = nums[i]
                i += 1
            res[k] = square * square
        
        return res
