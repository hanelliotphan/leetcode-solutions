class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        Logic: Set
        
        Time: O(n)
        Space: O(1)
        """
        return len(set(sentence)) == 26
