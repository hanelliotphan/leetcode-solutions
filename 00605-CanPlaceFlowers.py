# https://leetcode.com/problems/can-place-flowers/description/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Logic: Linear Scan

        Time: O(n)
        Space: O(1)
        """
        i = count = 0

        while i < len(flowerbed):
            if flowerbed[i] == 0 \
            and (i == 0 or flowerbed[i-1] == 0) \
            and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count += 1
            i += 1
        
        return count >= n
