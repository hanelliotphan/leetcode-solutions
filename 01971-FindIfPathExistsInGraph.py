# https://leetcode.com/problems/find-if-path-exists-in-graph/description/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Logic: Depth First Search

        Time: O(n+m)
        Space: O(n+m)
        """
        if [source, destination] in edges and [destination, source] in edges:
            return True
        
        directions = collections.defaultdict(list)
        visited = [0] * n

        for s, d in edges:
            directions[s].append(d)
            directions[d].append(s)
        
        def dfs(curr):
            if curr == destination:
                return True
            if not visited[curr]:
                visited[curr] += 1
                for next in directions[curr]:
                    if dfs(next):
                        return True
            return False
        
        return dfs(source)
