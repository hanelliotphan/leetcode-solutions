class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        """
        Logic: One pass

        Time: O(n)
        Space: O(1)
        """
        employee_id = logs[0][0]
        longest_task = logs[0][1]

        for i in range(1, len(logs)):
            duration = logs[i][1] - logs[i-1][1]
            if duration > longest_task:
                longest_task = duration
                employee_id = logs[i][0]
            elif duration == longest_task:
                employee_id = min(employee_id, logs[i][0])

        return employee_id
