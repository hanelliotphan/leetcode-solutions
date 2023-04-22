# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/description/

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        """
        Time: O(26*n) -- for n in range(s[1], s[4]+1)
        Space: O(26) --> O(1)
        """
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
                    "J", "K", "L", "M", "N", "O", "P", "Q", "R", 
                    "S", "T", "U", "V", "W", "X", "Y", "Z"]
        
        res = []
        start = alphabet.index(s[0])

        for i in range(start, len(alphabet)):
            j1 = int(s[1])
            j2 = int(s[4])
            for j in range(j1, j2+1):
                res.append(f"{alphabet[i]}{j}")
            if alphabet[i] == s[3]:
                break

        return res
