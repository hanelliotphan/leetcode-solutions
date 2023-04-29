# https://leetcode.com/problems/unique-morse-code-words/description/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_dict = {
            "a": ".-", "b": "-...", "c": "-.-.",
            "d": "-..", "e": ".", "f": "..-.",
            "g": "--.", "h": "....", "i": "..",
            "j": ".---", "k": "-.-","l": ".-..",
            "m": "--", "n": "-.", "o": "---",
            "p": ".--.", "q": "--.-", "r": ".-.", "s": "...",
            "t": "-", "u": "..-", "v": "...-",
            "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."
        }

        visited = set()

        for word in words:
            res = ""
            for ch in word:
                res += morse_dict[ch]
            visited.add(res)

        return len(visited)
