# https://leetcode.com/problems/high-five/description/

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        """
        Logic: Hash Map
        
        Time: O(n*logn)
        Space: O(n)
        """
        id_score = collections.defaultdict(list)
        res = []

        for student_id, score in items:
            id_score[student_id].append(score)
        
        for student_id, score in id_score.items():
            avg = int(sum(sorted(score, reverse=True)[:5]) / 5)
            res.append([student_id, avg])
        
        return sorted(res, key=lambda x: x[0])
