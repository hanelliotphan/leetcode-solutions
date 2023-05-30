# https://leetcode.com/problems/design-hashset/description/

class MyHashSet:
    """
    Logic: Brute Force
    
    Time: O(n)
    Space: O(n)
    """
    def __init__(self):
        self.set = []

    def add(self, key: int) -> None:
        self.set.append(key)

    def remove(self, key: int) -> None:
        i = 0
        while i < len(self.set):
            if self.set[i] == key:
                del self.set[i]
                i -= 1
            i += 1

    def contains(self, key: int) -> bool:
        return key in self.set
