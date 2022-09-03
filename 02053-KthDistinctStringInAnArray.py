class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        """
        Logic: Counter
        
        Time: O(n)
        Space: O(n)
        """
        counter = collections.Counter(arr)
        
        for key, val in counter.items():
            if val == 1:
                k -= 1
                if k == 0: return key
        
        return ""
