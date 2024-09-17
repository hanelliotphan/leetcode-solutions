class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """
        Logic: Brute Force

        Time: O(d*s)
        Space: O(s)
        """
        words = sentence.split()

        for i in range(len(words)):
            for d in dictionary:
                if words[i].startswith(d):
                    words[i] = d
        
        return ' '.join(words)
