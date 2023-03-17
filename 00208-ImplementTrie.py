"""
Logic: Brute Force

Time: O(max(word, prefix))
Space: O(nodes)
"""
class Trie:
    def __init__(self):
        self.nodes = collections.defaultdict(Trie)
        self.word_found = False
        
    def insert(self, word: str) -> None:
        obj = self
        for ch in word:
            obj = obj.nodes[ch]
        obj.word_found = True
        
    def search(self, word: str) -> bool:
        obj = self
        for ch in word:
            if ch not in obj.nodes:
                return False
            obj = obj.nodes[ch]
        return obj.word_found
    
    def startsWith(self, prefix: str) -> bool:
        obj = self
        for ch in prefix:
            if ch not in obj.nodes:
                return False
            obj = obj.nodes[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
