# https://leetcode.com/problems/merge-similar-items/description/

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        """
        Logic: Hash Map

        Time: O((n+m)*log(m+n))
        Space: O(n+m)
        """
        nodes = {}
        res = []

        for a, b in items1:
            nodes[a] = b
        
        for a, b in items2:
            if a in nodes:
                nodes[a] += b
            else:
                nodes[a] = b
        
        return sorted([[k, v] for k, v in nodes.items()])
