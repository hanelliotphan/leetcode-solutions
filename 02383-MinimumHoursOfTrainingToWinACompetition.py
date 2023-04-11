# https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/description/

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        count = 0

        for i in range(len(energy)):
            if initialEnergy <= energy[i]:
                training = energy[i] - initialEnergy
                initialEnergy = energy[i] + 1
                count += training + 1
            if initialExperience <= experience[i]:
                training = experience[i] - initialExperience
                initialExperience = experience[i] + 1
                count += training + 1
            initialEnergy -= energy[i]
            initialExperience += experience[i]
        
        return count
