
class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num != 0:
            if num % 2 == 1:
                num = num - 1
            else:
                num = num / 2
            res += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfSteps(8))
