# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Logic: Two Pointers
        
        Time: O(n)
        Space: O(n)
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i = 0; j = len(s)-1
        sa = [ch for ch in s]

        while i < j:
            if sa[i] in vowels and sa[j] in vowels:
                sa[i], sa[j] = sa[j], sa[i]
                i += 1
                j -= 1
            elif sa[i] in vowels and sa[j] not in vowels:
                j -= 1
            elif sa[i] not in vowels and sa[j] in vowels:
                i += 1
            else:
                i += 1
                j -= 1
            
        return "".join(sa)
