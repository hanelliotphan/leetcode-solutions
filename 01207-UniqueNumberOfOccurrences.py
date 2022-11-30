class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        Logic: Hash Map/Counter
        
        Time: O(n)
        Space: O(n)
        """
        counter = Counter(arr)
        visited = []
        
        for val in counter.values():
            if val not in visited:
                visited.append(val)
            else:
                return False
        
        return True
