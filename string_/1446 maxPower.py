class Solution:
    # todo 连续问题
    def maxPower(self, s: str) -> int:
        # 设置一个值记录当前的最大值和当前的频数.只记录频数即可
        # 设置一个值记录前一个值,用来判断是否连续
        res = []
        pre_key = None
        pre_value = 1
        for i in s:
            if i == pre_key:
                pre_value += 1
            elif i != pre_key:
                pre_key = i
                res.append(pre_value)
                pre_value = 1
        print(res)
        return max(res)


if __name__ == '__main__':
    s = "cc"
    sol = Solution()
    print(sol.maxPower(s))
