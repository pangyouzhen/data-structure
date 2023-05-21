class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        n = 0
        min_val = min(a, b)
        max_val = max(a, b)
        for i in range(1, min_val):
            if min_val % i == 0 and max_val % i == 0:
                n += 1
        return n


if __name__ == '__main__':
    func = Solution.commonFactors
