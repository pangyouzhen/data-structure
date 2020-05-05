import collections
from typing import List


class MagicDictionary(object):
    def __init__(self):
        self.buckets = collections.defaultdict(list)

    def buildDict(self, words):
        for word in words:
            self.buckets[len(word)].append(word)

    def search(self, word):
        return any(sum(a != b for a, b in zip(word, candidate)) == 1
                   for candidate in self.buckets[len(word)])


# Your MagicDictionary object will be instantiated and called as such:
if __name__ == '__main__':
    dict2 = ["hello", "leetcode"]
    obj = MagicDictionary()
    obj.buildDict(dict2)
    # print(obj.search("hello"))
    # print(obj.search("hhllo"))
    # print(obj.search("hell"))
    # print(obj.search("leetcoded"))
    print(obj.search("hlelo"))
