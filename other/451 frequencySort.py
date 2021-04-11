from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        # print(c.most_common())
        # new_c = sorted(c.items(), key=lambda x: x[1], reverse=True)
        res = [c[0] * c[1] for c in c.most_common()]
        return ''.join(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.frequencySort("tree"))
