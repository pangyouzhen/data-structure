class Solution:
    def maxPower(self, s: str) -> int:
        res = []
        pre = None
        pre_val = 0
        for i in s:
            if i == pre:
                pre_val += 1
            else:
                pre_val = 1
            res.append(pre_val)
            pre = i
        return max(res)


if __name__ == '__main__':
    s = "cc"
    sol = Solution()
    print(sol.maxPower(s))
