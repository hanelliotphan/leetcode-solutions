class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        """
        Logic: Prefix Sum with Defaultdict

        Time: O(n*max(frequencies))
        Space: O(n)
        """
        d = collections.defaultdict(list)
        res = [0]*len(nums)

        for i, n in enumerate(nums):
            d[n].append(i)

        for k, v in d.items():
            dist = 0
            for i in range(len(v)):
                dist += v[i]
                res[v[i]] += v[i]*(i+1)-dist
            dist = 0
            for i in range(len(v)-1, -1, -1):
                dist += v[i]
                res[v[i]] += dist-v[i]*(len(v)-i)
        
        return res
