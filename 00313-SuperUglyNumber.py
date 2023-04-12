# https://leetcode.com/problems/super-ugly-number/description/

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """
        Logic: Priority Queue (Min Heap)

        Time: O(n*logp)
        Space: O(n+p)
        """
        pq = [1]
        visited = {1}

        for _ in range(n-1):
            x = heapq.heappop(pq)
            for p in primes:
                if p*x not in visited:
                    visited.add(p*x)
                    heapq.heappush(pq, p*x)
                if x % p == 0:
                    break
            
        return heapq.heappop(pq)
