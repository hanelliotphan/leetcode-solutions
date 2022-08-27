class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        """
        Logic: Count
        
        Time: O(n)
        Space: O(s)
        """
        curr_s = ""
        count = 0
        
        for ch in s:
            curr_s += ch
            if curr_s in words:
                count += words.count(curr_s)
                
        return count
