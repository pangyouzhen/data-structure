class Solution:
    #  这个和17 不一样 的点在于这个nums 取出来之后会对原先的有影响,需要增加used进行判断
    #  递归树
    # def permute(self, nums):
    #     curr = []
    #     ans = []
    #
    #     def dfs(nums, d, n, used, one_ans, all_ans):
    #         if d == n:
    #             all_ans.append(one_ans[:])
    #             return
    #         for i in range(0, len(nums)):
    #             if used[i]:
    #                 continue
    #             used[i] = True
    #             one_ans.append(nums[i])
    #             dfs(nums, d + 1, n, used, one_ans, all_ans)
    #             one_ans.pop()
    #             used[i] = False
    #
    #     dfs(nums, 0, len(nums), [False] * len(nums), curr, ans)
    #     return ans
    #
    # def permute_rec_error(self, nums):
    #     global result
    #     result = []
    #     self.permute_rec_memo_error(nums, 0, [])
    #     return result
    #
    # def permute_rec_memo_error(self, nums, index, one_ans):
    #     if index == len(nums):
    #         result.append(one_ans)
    #         return
    #     for i, v in enumerate(nums):
    #         one_ans.append(v)
    #         print(f"self.permute_rec_memo_error({nums=},{index+1=},{one_ans=}")
    #         self.permute_rec_memo_error(nums, index + 1, one_ans)
    #     return

    def permute(self, nums):
        global result
        result = []
        self.permute_rec_memo(nums, 0, [], [False] * len(nums))
        return result

    def permute_rec_memo(self, nums, index, one_ans, used):
        if index == len(nums):
            result.append(one_ans[:])
            return
        for i, v in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            one_ans.append(nums[i])
            print(f"self.permute_rec_memo({nums=},{index+1=},{one_ans=},{used=}")
            self.permute_rec_memo(nums, index + 1, one_ans, used)
            # 这里回溯要把原先的数组也变回以前的
            one_ans.pop()
            used[i] = False
        return


# self.permute_rec_memo_error(nums, 0, [])
# self.permute_rec_memo_error(nums, 1, [1])
# self.permute_rec_memo_error(nums, 2, [1,1])
# self.permute_rec_memo_error(nums, 2, [1,1,2])
# self.permute_rec_memo_error(nums, 2, [1,1,2,3])
# self.permute_rec_memo_error(nums, 2, [1,1,2,3,2])
# ...
# self.permute_rec_memo_error(nums, 2, [1,1,2,3,2,1,2,3,3,1,2,3])
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
