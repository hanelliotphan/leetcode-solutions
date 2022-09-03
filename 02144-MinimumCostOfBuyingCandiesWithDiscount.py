# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        """
        Logic: Sort
        
        Time: O(n*logn)
        Space: O(1)
        """
        cost = sorted(cost, reverse=True)
        total, i, n = 0, 0, len(cost)
        
        while i < n:
            total += sum(cost[i:i+2])
            i += 3
            
        return total
