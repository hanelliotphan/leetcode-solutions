# https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = "qwertyuiopQWERTYUIOP"
        r2 = "asdfghjklASDFGHJKL"
        r3 = "zxcvbnmZXCVBNM"

        res = []

        for word in words:
            curr_r = 0
            flag = False
            for ch in word:
                if curr_r == 0:
                    if ch in r1: curr_r = 1
                    elif ch in r2: curr_r = 2
                    elif ch in r3: curr_r = 3
                else:
                    if (curr_r == 1 and ch in r1) \
                    or (curr_r == 2 and ch in r2) \
                    or (curr_r == 3 and ch in r3):
                        continue
                    else:
                        flag = True
                        break
            if flag: continue
            else: res.append(word)

        return res
