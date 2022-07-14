class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Logic: Pythagorean Theorem + Sort
        
        Time: O(n logn)
        Space: O(1)
        """
        points.sort(key=lambda p: p[0]*p[0] + p[1]*p[1])
        return points[:k]
