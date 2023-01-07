class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Logic: One Pass

        Time: O(n)
        Space: O(1)
        """
        if len(gas) != len(cost): return -1
        station = 0
        curr_tank = total_tank = 0

        for i in range(len(gas)):
            curr_tank += gas[i] - cost[i]
            total_tank += gas[i] - cost[i]
            if curr_tank < 0:
                station = i + 1
                curr_tank = 0

        return station if total_tank >= 0 else -1
