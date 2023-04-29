# https://leetcode.com/problems/remove-letter-to-equalize-frequency/description/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        """
        Logic: Hash Map/Counter
        
        Time: O(n)
        Space: O(n)
        """
        counter = collections.Counter(word)

        for ch in word:
            counter[ch] -= 1
            if counter[ch] == 0:
                counter.pop(ch)
            if len(set(counter.values())) == 1:
                return True
            counter[ch] += 1
    
        return False
