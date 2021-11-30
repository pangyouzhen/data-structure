import collections
from functools import reduce
from typing import List, Optional, Dict

class Solution:
    def replaceWords(self, roots, sentence):
        rootset = set(roots)

        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))


class Solution2(object):
    def replaceWords(self, roots, sentence):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for root in roots:
            reduce(dict.__getitem__, root, trie)[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur: break
                cur = cur[letter]
            return cur.get(END, word)

        return " ".join(map(replace, sentence.split()))

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        p = self.root
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p["#"] = "end"

    def find(self, prefix: str) -> Optional[Dict]:
        p = self.root
        for c in prefix:
            if c not in p: return None
            p = p[c]
        return p

    def findAllWords(self, prefix: str) -> Optional[List]:
        p = self.find(prefix)
        if p:
            result = self.list_words(p)
            res = [prefix + i for i in result]
            return res

    def list_words(self, trie: Dict) -> List:
        my_list = []
        for k, v in trie.items():
            if k != '#':
                for el in self.list_words(v):
                    my_list.append(k + el)
            else:
                my_list.append('')
        return my_list


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("apkinstall")
    trie.insert("bde")
    print(trie.find("a"))
    print(trie.findAllWords("a"))
    sol = Solution()
    print(sol.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery"))
    sol2 = Solution2()
    print(sol2.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery"))