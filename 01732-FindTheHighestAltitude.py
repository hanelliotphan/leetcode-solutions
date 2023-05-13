# https://leetcode.com/problems/find-the-highest-altitude/description/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        max_alt = 0
        curr_alt = 0

        for x in gain:
            curr_alt += x
            max_alt = max(max_alt, curr_alt)
        
        return max_alt
