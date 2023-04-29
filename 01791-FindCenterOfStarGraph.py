# https://leetcode.com/problems/find-center-of-star-graph/description/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        Logic: Hash Map
        
        Time: O(E + V)
        Space: O(V)
        """
        hm = collections.defaultdict(list)

        for u, v in edges:
            hm[u].append(v)
            hm[v].append(u)
        
        for k, v in hm.items():
            if len(v) == len(hm)-1:
                return k
        
        return None
