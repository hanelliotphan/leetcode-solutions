class Solution:
    def digitSum(self, s: str, k: int) -> str:
        """
        Logic: Accummulation
        
        Time: O(n)
        Space: O(k)
        """
        while len(s) > k:
            set_k = [s[i:i+k] for i in range(0, len(s), k)]
            s = ''
            for each_s in set_k:
                s += str(sum([int(ch) for ch in each_s]))
        
        return s
