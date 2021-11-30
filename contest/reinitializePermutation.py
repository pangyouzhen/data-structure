import copy


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        raw = [i for i in range(n)]

        def step(perm):
            n = len(perm)
            a = [None] * n
            for i in range(n):
                if i % 2 == 0:
                    a[i] = perm[int(i / 2)]
                else:
                    a[i] = perm[int(n / 2) + int((i - 1) / 2)]
            return a

        a = copy.deepcopy(raw)
        perm = step(a)
        res = 1

        while perm != raw:
            perm = step(perm)
            res += 1
        return res


if __name__ == '__main__':
    n = 6
    sol = Solution()
    print(sol.reinitializePermutation(n))
