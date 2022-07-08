class Solution:
    def digitCount(self, num: str) -> bool:
        """
        Logic: Hash Map of Indices & Frequencies
        
        Time: O(n)
        Space: O(n)
        """
        counter = dict()
        
        for n in num:
            if int(n) not in counter:
                counter[int(n)] = 1
            else:
                counter[int(n)] += 1
                
        for i in range(len(num)):
            if i not in counter:
                counter[i] = 0
                
        for i in range(len(num)):
            if i in counter and counter[i] != int(num[i]):
                return False
            
        return True
