class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Logic: Hash Map
        
        Time: O(n*logn)
        Space: O(n)
        """
        hash_map = {}
        
        for word in words:
            if word not in hash_map:
                hash_map[word] = 1
            else:
                hash_map[word] += 1
        
        res = sorted(hash_map, key=lambda x: (-hash_map[x], x))
        return res[:k]
