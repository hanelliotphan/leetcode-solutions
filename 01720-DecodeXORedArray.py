class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        """
        Logic: Inverse XOR = XOR
        
        Time: O(n)
        Space: O(1)
        """
        res = [first]
        
        for n in encoded:
            res.append(n ^ res[-1])
            
        return res
