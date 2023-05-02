class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        """
        Logic: Hash Map
        
        Time: O(n+m)
        Space: O(n+m)
        """
        s1 = s1.split()
        s2 = s2.split()
        hm = collections.defaultdict(int)
        res = []

        for word in s1:
            hm[word] += 1
        
        for word in s2:
            hm[word] += 1
        
        for k, v in hm.items():
            if v == 1:
                res.append(k)
        
        return res
