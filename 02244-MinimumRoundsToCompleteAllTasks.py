# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        """
        Logic: Hash Map/Counter

        Time: O(n)
        Space: O(n)
        """
        num_round = 0
        counter = collections.Counter(tasks)

        for v in counter.values():
            if v < 2:
                return -1
            else:
                num_round += (v // 3 + min(1, v % 3))
        
        return num_round
