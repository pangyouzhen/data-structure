from string import ascii_uppercase


# 记忆化搜索，递归
# 动态规划的算法来做，爬楼梯
# todo
class Solution:
    def numDecodings(self, s: str) -> int:
        res = []

        def bt(s, one_ans):
            res.append(one_ans[:])
            for i, v in enumerate(s):
                one_ans.append(v)
                bt(s[i:], one_ans)
                one_ans.pop()

        one_ans = []
        bt(s, one_ans)
        print(res)
        return len(res)


if __name__ == '__main__':
    # nums = "12"
    sol = Solution()
    # print(sol.numDecodings(nums))
    nums2 = "226"
    print(sol.numDecodings(nums2))
# 226-> / + 226 ->  2 + 26  -> 22 + 6 +
#  26 ->  2 + 6
