# https://leetcode.com/problems/defanging-an-ip-address/description/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        res = ""
        
        for ch in address:
            if ch != ".":
                res += ch
            else:
                res += "[.]"
        
        return res
