class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """
        Logic: Prefix XOR with linear scan

        Time: O(a+q)
        Space: O(1)
        """
        res = []
        
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]

        for x, y in queries:
            if x > 0: res.append(arr[x-1]^arr[y])
            else: res.append(arr[y])
        
        return res
