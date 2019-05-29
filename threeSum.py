class Solution:

    def __init__(self, target):
        self.target = target

    # def threeSum(self, nums):
    #     res = []
    #     for i, v in enumerate(nums):
    #         twoTarget = self.target - v
    #         twoNums = nums[i + 1:]
    #         if len(twoNums) > 0:
    #             for ti, tv in enumerate(twoNums):
    #                 if ((twoTarget - tv) in twoNums and (twoNums.index(twoTarget - tv) != ti)):
    #                     ls = sorted([v, tv, twoTarget - tv])
    #                     if ls not in res:
    #                         res.append(ls)
    #     return res
    # 超时了,利用  twoSum

    def threeSum(self, nums):
        res = []
        sort_nums = sorted(nums)
        i = 0
        while (i < len(nums) - 1):
            if (sort_nums[i] == sort_nums[i + 1]):
                i = i + 1
            else:
                twoTarget = self.target - sort_nums[i]
                twoNums = sort_nums[i + 1:]
                if len(twoNums) > 0:
                    for ti, tv in enumerate(twoNums):
                        if ((twoTarget - tv) in twoNums and (twoNums.index(twoTarget - tv) != ti)):
                            print("%s %s %s" % (i, twoNums, twoTarget))
                            ls = sorted([nums[i], tv, twoTarget - tv])
                            if ls not in res:
                                res.append(ls)
                i = i + 1
        return res


if __name__ == '__main__':
    sol = Solution(0)
    res = sol.threeSum([-1, 0, 1, 2, -1, -4])
    print(res)
