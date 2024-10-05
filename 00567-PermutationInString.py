class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Logic: Sliding Window
        
        Time: O(m*n)
        Space: O(m*n)
        """
        l1 = len(s1)
        C1 = collections.Counter(s1)
        
        for i in range(len(s2)+l1):
            C2 = collections.Counter(s2[i:i+l1])
            if C1 == C2:
                return True
            
        return False
