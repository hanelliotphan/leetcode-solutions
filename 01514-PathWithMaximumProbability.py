# https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        """
        Logic: Priority Queue

        Time: O(n+e^2)
        Space: O(n+e)
        """
        directions = collections.defaultdict(list)

        for i, sd in enumerate(edges):
            s, d = sd
            directions[d].append((s, i))
            directions[s].append((d, i))
        
        probs = [0.0] * n
        probs[start] = 1.0
        q = collections.deque([start])

        while q:
            curr = q.popleft()
            for nei, i in directions[curr]:
                if probs[curr] * succProb[i] > probs[nei]:
                    probs[nei] = probs[curr] * succProb[i]
                    q.append(nei)
        
        return probs[end]
