# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        """
        Logic: Brute Force

        Time: O(n*r)
        Space: O(n)
        """
        res = []
        
        for n in range(left, right+1):
            visited = []
            for a, b in ranges:
                visited.append(a <= n <= b)
            res.append(any(visited))
        
        return all(res)
