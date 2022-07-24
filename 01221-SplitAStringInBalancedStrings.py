class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """
        Logic: Increment/decrement for balance
        
        Time: O(n)
        Space: O(1)
        """
        count = tmp = 0
        
        for ch in s:
            if ch == "R":
                tmp += 1
            elif ch == "L":
                tmp -= 1
            if tmp == 0:
                count += 1
                
        return count
