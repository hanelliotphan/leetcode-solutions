# https://leetcode.com/problems/fixed-point/description/

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for i, n in enumerate(arr):
            if n == i: return i
        
        return -1
