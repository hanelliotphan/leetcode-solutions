class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        Logic: Hash Map/Counter
        
        Time: O(1)
        Space: O(n)
        """
        counter = collections.Counter(text)
        
        return min(counter["b"], counter["a"], counter["l"]//2, 
                   counter["o"]//2, counter["n"])
