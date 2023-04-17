# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1) --> need to return `res`, no extra space needed for the implementation
        """
        res = []

        for candy in candies:
            if candy + extraCandies >= max(candies):
                res.append(True)
            else:
                res.append(False)
        
        return res
