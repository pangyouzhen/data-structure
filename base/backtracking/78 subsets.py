from typing import List


# combination


class Solution:
    def __init__(self):
        self.res = []

    def subsets(self, nums):
        one_ans = []
        start = 0
        self.nums_len = len(nums)
        self.subsets_memo(nums, start, one_ans)
        return self.res

    def subsets_memo(self, nums, start, one_ans):
        # 这里的回溯的终止条件不太一样
        self.res.append(one_ans[:])
        for i in range(start, self.nums_len):
            print(f"{'**' * (start + 1)}for {i = } in {range(start, self.nums_len) = }")
            one_ans.append(nums[i])
            self.subsets_memo(nums, i + 1, one_ans)
            one_ans.pop()
            print("_____________________")
        return


# 回溯方法模板
# backtracking() {
#     if (终止条件) {
#         存放结果;
#     }
#
#     for (选择：选择列表（可以想成树中节点孩子的数量）) {
#         递归，处理节点;
#         backtracking();
#         回溯，撤销处理结果
#     }
# }
# 本题的终止条件： 求取子集问题，其实没有必要加终止条件，因为子集就是要遍历整个一棵树，不需要任何剪枝！
# 因为求子集也是无序的，所以for循环要从startIndex开始！


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    print(sol.subsets(nums))
