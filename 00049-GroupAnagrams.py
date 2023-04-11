# https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Logic: Hash Map

        Time: O(n)
        Space: O(26) --> O(1)
        """
        res = collections.defaultdict(list)
        
        for str in strs:
            counter = [0] * 26
            for ch in str:
                counter[ord(ch)-ord('a')] += 1
            res[tuple(counter)].append(str)

        return list(res.values())
