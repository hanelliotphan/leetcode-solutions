class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        """
        Logic: Sorting

        Time: O(n*logn)
        Space: O(1)
        """
        if len(skill) == 2:
            return skill[0] * skill[1]
            
        skill.sort()
        skill_per_team = skill[0] + skill[-1]
        chem = 0

        for i in range(len(skill) // 2):
            if skill[i] + skill[-(i+1)] != skill_per_team:
                return -1
            chem += (skill[i] * skill[-(i+1)])

        return chem
