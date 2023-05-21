class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        n_int = [int(i) for i in str(n)][::-1]
        s = sum(n_int)
        if s <= target:
            return 0
        else:
            minus = s - target
            iter_count = 0
            for i in n_int:
                m = minus - i + 1
                if i > 0:
                    iter_count += 1
                    minus = m
                else:
                    break
            for i in range(iter_count - 1):
                n_int[i] = 0
            n_int[iter_count - 1] += 1
        return int(''.join([str(i) for i in n_int[::-1]])) - n


if __name__ == '__main__':
    func = Solution().makeIntegerBeautiful
    # n = 423
    # target = 6
    n = 8
    target = 2
    print(func(n, target))
