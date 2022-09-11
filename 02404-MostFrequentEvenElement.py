# https://leetcode.com/problems/most-frequent-even-element/

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        """
        Logic: Hash Map
        
        Time: O(n)
        Space: O(n)
        """
        freqs = dict()
        
        for n in nums:
            if n % 2 == 0 and n not in freqs:
                freqs[n] = 1
            elif n % 2 == 0 and n in freqs:
                freqs[n] += 1
                    
        curr_max_freq = float("-inf")
        curr_min_num = float("inf")
        
        for k, v in freqs.items():
            if v == max(list(freqs.values())):
                curr_min_num = min(curr_min_num, k)
                
        return curr_min_num if curr_min_num != float("inf") else -1
