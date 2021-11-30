from typing import Dict, Union, Optional, List


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

    def find_word(self, prefix: str) -> List[str]:
        res = []
        word_dict = self.find(prefix)

        # 回溯法找所有可能的单词

        def bt(value, one_ans, res):
            if value is True:
                res.append("".join(one_ans[:-1]))
                return
            for i in value.keys():
                one_ans.append(i)
                bt(value[i], one_ans, res)
                one_ans.pop()

        one_ans = [prefix]
        bt(word_dict, one_ans, res)
        return res

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) is not None


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("apkinstall")
    trie.insert("bde")
    print("find", trie.find("a"))
    print("search", trie.search("ap"))
    print("startswith", trie.startsWith("ap"))
    print(trie.search("affff"))
    print(trie.find_word("b"))
