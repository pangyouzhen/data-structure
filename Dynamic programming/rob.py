# 实际问题转化为数学递归问题
# 现在假设现在是最大值，增加新的元素应该怎么得到最大值

def rob(n, ls):
    if n == 1:
        res = ls[0]
    else:
        res = max(rob(n - 1, ls) + ls[n], rob(n - 1, ls))
    return res


# 大问题转化为小问题，如何将大问题与小问题关联
# class Solution:
#     def rob(self, nums):
#         t = len(nums)
#         a = 0
#         while a < t:
#             a = a + 1
#         # ls_1 = [nums[i] for i in range(0, t, 2)]
#         # ls_2 = [nums[i] for i in range(1, t, 2)]
#         # print(ls_1, ls_2)
#         # return max(sum(ls_1), sum(ls_2))
#         pass


if __name__ == '__main__':
    # assert rob([1, 2, 3, 1]) == [1, 3]
    # assert rob([2, 7, 9, 3, 1]) == 12
    assert rob(1, [2, 1, 1, 2]) == [2]
