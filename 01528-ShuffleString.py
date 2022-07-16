class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        """
        Logic: Placeholder array
        
        Time: O(n)
        Space: O(n)
        """
        res = [''] * len(s)
        
        for i, c in enumerate(s):
            res[indices[i]] = c
            
        return "".join(res)
