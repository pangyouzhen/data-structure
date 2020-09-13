from string import ascii_uppercase


#  error
# 记忆化搜索，递归
# 动态规划的算法来做，爬楼梯
class Solution:
    # def __init__(self):
    #     self.nums_str = [str(i) for i in range(1, 27)]
    #     self.res = []
    #
    # def numDecodings(self, s: str) -> int:
    #     one_ans = []
    #     start = 0
    #     self.numDecodings_memo(s, start, one_ans)
    #     print(self.res)
    #     return len(self.res)
    #
    # def numDecodings_memo(self, s, index, one_ans):
    #     if index == len(s):
    #         self.res.append(one_ans[:])
    #         return
    #     for i in range(1, len(s)):
    #         print(f"{'++  ' * index}for {i=} in {range(1,len(s))= }")
    #         print(f'{index = },{i=},{s[index:i] = }')
    #         if s[index:i] not in self.nums_str:
    #             continue
    #         one_ans.append(s[index:i])
    #         print(f'{one_ans =}')
    #         print(f"----------------------")
    #         s = s[index:]
    #         self.numDecodings_memo(s, index + 1, one_ans)
    #         s = s[index - 1:]
    #         one_ans.pop()
    #     return
    pass


if __name__ == '__main__':
    # nums = "12"
    sol = Solution()
    # print(sol.numDecodings(nums))
    nums2 = "226"
    print(sol.numDecodings(nums2))
# 226-> / + 226 ->  2 + 26  -> 22 + 6 +
#  26 ->  2 + 6
