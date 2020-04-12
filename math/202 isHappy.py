class Solution:
    def isHappy(self, n: int) -> bool:
        s = {n}
        while n != 1:
            tmp = sum([int(i) ** 2 for i in str(n)])
            if tmp in s:
                return False
            s.add(tmp)
            n = tmp
        return True


if __name__ == '__main__':
    sol = Solution()
    assert sol.isHappy(19) is True
    assert sol.isHappy(1) is True
    assert sol.isHappy(2) is False
