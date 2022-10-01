class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        num_lonely_pixels = 0
        col = 0
        
        for col in zip(*picture):
            if col.count("B") == 1:
                idx = col.index("B")
                if picture[idx].count("B") == 1:
                    num_lonely_pixels += 1
                        
        return num_lonely_pixels
