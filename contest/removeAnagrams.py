from collections import Counter


class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        pre = None
        res = []
        for i, v in enumerate(words):
            c = Counter(v)
            if c != pre:
                pre = c
                res.append(v)
        return res
