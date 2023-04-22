# https://leetcode.com/problems/reformat-date/description/

class Solution:
    def reformatDate(self, date: str) -> str:
        """
        Logic: Brute Force
        
        Time: O(1)
        Space: O(1)
        """
        months = {
            "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
            "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
            "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
        }
        d, m, y = date.split()
        d = d[:-2] if len(d) > 3 else f"0{d[:-2]}"
        m = str(months[m]) if months[m] >= 10 else f"0{months[m]}"

        return "-".join((y, m, d)) 
