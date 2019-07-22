class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # apple: {"a":"pple"}}}}}
        # apple: {"a":{"p":{"ple"}}}}}
        # apple: {"a":{"p":{"p":{"le"}}}}}
        p = self.root
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p["#"] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """


# Your Trie object will be instantiated and called as such:
if __name__ == '__main__':
    obj = Trie()
    obj.insert("apple")
    obj.insert("test")
    # param_2 = obj.search("apple")
    # param_3 = obj.startsWith("app")
