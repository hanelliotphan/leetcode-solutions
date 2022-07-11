class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Logic: Have two variables `curr_max` and `all_max` to store profits
        
        Time: O(n)
        Space: O(1)
        """
        curr_max, all_max = 0, 0
        
        for i in range(1, len(prices)):
            potential_benefit = curr_max + (prices[i] - prices[i-1])
            curr_max = max(potential_benefit, 0)
            all_max = max(curr_max, all_max)
            
        return all_max
