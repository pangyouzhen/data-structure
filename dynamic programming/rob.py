# 实际问题转化为数学递归问题
# 现在假设现在是最大值，增加新的元素应该怎么得到最大值
# TODO
# def rob_n(n, ls):
#     if n == 0:
#         res = ls[0]
#     elif n == 1:
#         res = ls[1]
#     else:
#         print(n)
#         res = max(rob_n(n - 2, ls) + ls[n], rob_n(n - 1, ls))
#         # 4 element n=3 index from 0
#         # ls[1] + ls[3] | ls[2]
#         #
#         print("-------------")
#     return res
#
#
# def rob(ls):
#     n = len(ls) - 1
#     return rob_n(n, ls)



# 动态规划的算法最好画表格，画树，表格有一般有两行，一个是index一个是需要求得值，一个简单的技巧使用memo  memo = [None] * (len(nums) + 1)



class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        memo = [None] * (len(nums) + 1)
        return self.rob_memo(nums, memo)

    def rob_memo(self, nums, memo):
        memo[0] = 0
        memo[1] = nums[0]
        for i, v in enumerate(nums[:-1]):
            memo[i + 2] = max(memo[i + 1], memo[i] + nums[i + 1])
        return memo[-1]


if __name__ == '__main__':
    res = Solution().rob
    assert res([2, 3, 8, 6, 7]) == 17
    assert res([2, 1, 1, 2]) == 4
    assert res([1, 2, 3, 1]) == 4
    assert res([2, 7, 9, 3, 1]) == 12
    assert res([1, 2, 3, 1]) == 4
