from typing import Dict, Union, Optional


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        p = self.root
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p["#"] = True

    def search(self, word: str) -> bool:
        node = self.find(word)
        return node is not None and "#" in node

    def find(self, prefix: str) -> Optional[Dict]:
        p = self.root
        for c in prefix:
            if c not in p: return None
            p = p[c]
        return p

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) is not None


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("apkinstall")
    trie.insert("bde")
    print(trie.find("a"))
    print(trie.search("ap"))
    print(trie.startsWith("ap"))
