class Solution:
    def reformatNumber(self, number: str) -> str:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        number = number.replace(" ", "")
        number = number.replace("-", "")
        
        res = ""
        
        for i in range(0, len(number), 3):
            if len(number[i:]) > 4:
                res += number[i:i+3]
                if i != len(number)-1:
                    res += "-"
            else:
                if len(number[i:]) == 4:
                    res += number[i:i+2]
                    res += "-"
                    res += number[i+2:]
                elif len(number[i:]) == 3 or len(number[i:]) == 2:
                    res += number[i:i+3]

        return res
