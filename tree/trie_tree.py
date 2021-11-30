class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here
        """
        self.root = {}

    def insert(self, word):
        """
        Insert a word into the trie
        :param word: str
        """
        p = self.root
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p["#"] = True

    def search(self, word):
        """
        Returns if the word is in the trie
        :param word:  str
        :rtype: bool
        """
        node = self.find(word)
        return node is not None and "#" in node

    def startsWith(self, prefix):
        """
    Reutrns if there is any word in the trie that starts with the given prefix
        :param prefix: str
        :return :bool
        """
        return self.find(prefix) is not None

    def find(self, prefix):
        p = self.root
        for c in prefix:
            if c not in p:
                return None
            p = p[c]
        return p


if __name__ == '__main__':
    sol = Trie()
    sol.insert("word")
    sol.insert("world")
    sol.insert("wow")
    sol.insert("www")
    sol.search("w")
    sol.search("wwl")
