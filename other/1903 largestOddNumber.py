class Solution:
    # 超时
    def largestOddNumber_(self, num: str) -> str:
        l = len(num)
        res = []
        for i in range(l):
            for j in range(i + 1, l + 1):
                if num[i:j] and int(num[i:j]) % 2 == 1:
                    res.append(int(num[i:j]))
        return str(max(res))

    def largestOddNumber(self, num: str) -> str:
        res = []
        for i, v in enumerate(num):
            if int(v) % 2 == 1:
                res.append(i)
        if not res:
            return ""
        max_value = max(res)
        return num[:max_value + 1]


if __name__ == '__main__':
    func = Solution().largestOddNumber
    num = "35412"
    print(func(num))
