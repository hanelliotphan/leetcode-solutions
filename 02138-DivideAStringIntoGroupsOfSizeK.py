# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/description/

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        """
        Logic: Brute Force
        
        Time: O(n//k)
        Space: O(1)
        """
        res = []

        for i in range(0, len(s), k):
            res.append(s[i:i+k])

        if len(res[-1]) < k:
            need_fill = k - len(res[-1])
            res[-1] += (fill*need_fill)
        
        return res
