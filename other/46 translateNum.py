class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            tmp = s[i - 2:i]
            c = a + b if "10" <= tmp <= "25" else a
            b = a
            a = c
        return a


#  这个是动态规划，试一下回溯算法？


if __name__ == '__main__':
    sol = Solution()
    print(sol.translateNum(12258))
