class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums):
        # 路径记录在one_ans中
        one_ans = []
        self.permute_rec_memo(nums, one_ans)
        return self.res

    def permute_rec_memo(self, nums, one_ans):
        if len(one_ans) == len(nums):
            self.res.append(one_ans[:])
            return
        for i in range(len(nums)):
            # 排除不合法的选择
            if nums[i] in one_ans:
                continue
            # 做选择
            one_ans.append(nums[i])
            # 进入下一层决策树
            self.permute_rec_memo(nums, one_ans)
            # 取消选择
            one_ans.pop()
        return


if __name__ == '__main__':
    sol = Solution()
    # print(sol.permute([1, 2, 3]))
    # a = sol.permute_rec_error([1, 2, 3])
    # print(len(a))
    # print(len(a[0]))
    # print(a)
    # 这里a的长度为什么是27，a[0]的长度是39
    b = sol.permute([1, 2, 3])
    print(b)
