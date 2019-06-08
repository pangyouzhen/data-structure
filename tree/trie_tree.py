class TrieNode(object):
    pass


class Trie:
    def __int__(self):
        """
        Initialize your data structure here
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the trie
        :param word: str
        """
        node = self.root
        for chars in word:
            child = node.data.get(chars)
            if not child:
                node.data[chars] = TrieNode()
            node = node.data[chars]
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie
        :param word:  str
        :rtype: bool
        """
        node = self.root
        for chars in word:
            node = node.data.get(chars)
            if not node:
                return False
        return node.is_word

    def startsWith(self, prefix):
        """
    Reutrns if there is any word in the trie that starts with the given prefix
        :param prefix: str
        :return :bool
        """
