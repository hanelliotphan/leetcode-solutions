# https://leetcode.com/problems/maximum-population-year/description/

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        """
        Logic: Hash Map
        
        Time: O(n)
        Space: O(n)
        """
        hm = collections.defaultdict(int)

        for b, d in logs:
            for i in range(b, d):
                hm[i] += 1
        
        max_pop = max(hm.values())
        year = max(hm.keys())

        for k, v in hm.items():
            if v == max_pop and k < year:
                year = k
        
        return year
