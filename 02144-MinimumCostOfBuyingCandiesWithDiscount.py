# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description/

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        """
        Logic: Brute Force with Sort
        
        Time: O(n*logn)
        Space: O(1)
        """
        cost.sort(reverse=True)
        total = 0
        i = 0

        for c in cost:
            if i == 2:
                i = 0
                continue
            total += c
            i += 1
        
        return total
