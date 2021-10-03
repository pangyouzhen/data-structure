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
        # 纵向，因为是取所有的子集，所以这里的没有终止条件
        self.res.append(one_ans[:])
        for i in range(start, self.nums_len):
            one_ans.append(nums[i])
            self.subsets_memo(nums, i + 1, one_ans)
            one_ans.pop()
        return


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    print(sol.subsets(nums))
