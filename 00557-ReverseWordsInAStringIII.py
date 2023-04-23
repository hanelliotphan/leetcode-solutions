# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([c[::-1] for c in s.split()])
