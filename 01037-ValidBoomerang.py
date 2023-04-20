# https://leetcode.com/problems/valid-boomerang/description/

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        """
        Logic: Mathematical Approach

        Time: O(1)
        Space: O(1)
        """
        return (points[0][0]-points[1][0]) * (points[0][1]-points[2][1]) \
                != (points[0][0]-points[2][0]) * (points[0][1] - points[1][1])
