class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:'
        """
        Logic: Hash Map/Counter
        
        Time: O(n*logn+k)
        Space: O(n)
        """
        counter = collections.Counter(nums)
        counter = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1])}
        res = []
        
        print(counter)

        for i in range(1, k+1):
            res.append(list(counter.keys())[-i])

        return res
