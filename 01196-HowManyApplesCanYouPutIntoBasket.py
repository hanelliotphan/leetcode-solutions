class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        """
        Logic: Counting Sort

        Time: O(n)
        Space: O(n)
        """
        count = [0]*1001
        curr_weight = apples = 0

        for w in weight:
            count[w] += 1
        
        for i in range(1, 1001):
            while curr_weight + i <= 5000 and count[i] > 0:
                count[i] -= 1
                curr_weight += i
                apples += 1
            if curr_weight + i > 5000:
                break
        
        return apples
