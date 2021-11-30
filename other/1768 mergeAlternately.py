class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        min_len = min(m, n)
        res = []
        for i in range(min_len):
            w1 = word1[i]
            w2 = word2[i]
            res.append(w1)
            res.append(w2)
        if m == n:
            return "".join(res)
        if min_len == m:
            return "".join(res) + word2[min_len:]
        if min_len == n:
            return "".join(res) + word1[min_len:]


if __name__ == '__main__':
    word1 = "abc"
    word2 = "pqr"
    sol = Solution()
    print(sol.mergeAlternately(word1, word2))
