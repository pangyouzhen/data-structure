from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = []
        for i in range(len(words)):
            for j in range(i, len(words)):
                if not (set(words[i]) & set(words[j])):
                    l = len(words[i])
                    a = len(words[j])
                    res.append(l * a)
        if res:
            return max(res)
        return 0


if __name__ == '__main__':
    # words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    func = Solution().maxProduct
    print(func(words))
