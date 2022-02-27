from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c_s = Counter(s)
        c_t = Counter(t)
        res = 0
        if c_s == c_t:
            return res
        else:
            keys = c_s.keys() | c_t.keys()
            for k in keys:
                if k in c_s.keys() and k in c_t.keys():
                    m = max(c_s[k], c_t[k])
                    res += 2 * m - c_s[k] - c_t[k]
                elif k not in c_s.keys():
                    res += c_t[k]
                else:
                    res += c_s[k]
            return res


if __name__ == '__main__':
    s = "leetcode"
    t = "coats"
    sol = Solution()
    print(sol.minSteps(s, t))
