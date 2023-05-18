# https://leetcode.com/problems/most-frequent-even-element/description/

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        """
        Logic: Hash Map/Counter
        
        Time: O(n)
        Space: O(n)
        """
        even = collections.defaultdict(int)

        for n in nums:
            if n % 2 == 0:
                even[n] += 1
        
        mx = -1
        smallest = float("inf")

        for k, v in even.items():
            if v > mx:
                mx = v
                smallest = k
            elif v == mx:
                smallest = min(smallest, k)
        
        return smallest if smallest != float("inf") else -1
