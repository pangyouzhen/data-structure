import pysnooper

class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums):
        one_ans = []
        self.permute_rec_memo(nums, one_ans)
        return self.res

    @pysnooper.snoop()
    def permute_rec_memo(self, nums, one_ans):
        # 纵向，因为是取2个元素，所以终止条件是
        if len(one_ans) == len(nums):
            self.res.append(one_ans[:])
            return
        # 横向循环。确保只循环一次
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
