class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Logic: Dynamic Programming
            (inspired by Fibonacci number problem)
        
        Time: O(n)
        Space: O(1)
        """
        prev, curr = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            total = cost[i] + min(prev, curr)
            prev = curr
            curr = total
            
        return min(prev, curr)
