# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description/

class Solution:
    def minMaxDifference(self, num: int) -> int:
        """
        Logic: Brute Force - Replace max with 9s and min with 0s

        Time: O(1)
        Space: O(1)
        """
        str_num = str(num)
        i = 0

        while str_num[i] == "9" and i < len(str_num)-1:
            i += 1

        return int(str_num.replace(str_num[i], "9")) - int(str_num.replace(str_num[0], "0"))
