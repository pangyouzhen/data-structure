class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        a = list(str(num))
        a = int("".join(a[::-1]))
        a = list(str(a))
        a = int("".join(a[::-1]))
        if a == num:
            return True
        return False


if __name__ == '__main__':
    func = Solution().isSameAfterReversals
    num = 526
    print(func(num))
