class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        """
        Logic: Two Pointers with Sorting

        Time: O(p*logp + t*logt)
        Space: O(1)
        """
        players.sort()
        trainers.sort()
        res = i = j = 0

        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                res += 1
                i += 1
            j += 1

        return res
