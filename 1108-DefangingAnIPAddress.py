class Solution:
    def defangIPaddr(self, address: str) -> str:
        """
        Logic: List of IP figures
        
        Time: O(n)
        Space: O(1) --> 4 figures only
        """
        i = 0
        res = []
        curr_str = ""
        
        while i < len(address):
            if address[i] != '.':
                curr_str += address[i]
            else:
                res.append(curr_str)
                curr_str = ""
            i += 1
        
        res.append(curr_str)
        
        return "[.]".join(res)
