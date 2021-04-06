class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums):
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
            one_ans.append(nums[i])
            self.permute_rec_memo(nums, one_ans)
            one_ans.pop()
        return


if __name__ == '__main__':
    sol = Solution()
    b = sol.permute([1, 2, 3])
    print(b)
