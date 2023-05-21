from typing import List


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefix_dict = {}
        res = []
        for word in words:
            n = 0
            for i in range(1, len(word)):
                prefix = word[:i]
                if prefix in prefix_dict.keys():
                    c = prefix_dict[prefix]
                    n += c
                    break
                c = 0
                if prefix:
                    for word in words:
                        if prefix in word:
                            c += 1
                prefix_dict[prefix] = c
                n += c
            res.append(n)
        return res

if __name__ == '__main__':
    func = Solution().sumPrefixScores
    words = ["abc", "ab", "bc", "b"]
    print(func(words))
