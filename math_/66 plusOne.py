class Solution:
    def plusOne(self, digits):
        _ = int(''.join(map(str, digits)))
        return list(map(int, list(str(_ + 1))))


if __name__ == '__main__':
    sol = Solution()
    digits = [1, 2, 3]
    res = sol.plusOne(digits)
    print(res)
