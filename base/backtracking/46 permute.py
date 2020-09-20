class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums):
        self.permute_rec_memo(nums, 0, [], [False] * len(nums))
        return self.res

    def permute_rec_memo(self, nums, index, one_ans, used):
        if index == len(nums):
            self.res.append(one_ans[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            one_ans.append(nums[i])
            print(f"self.permute_rec_memo({nums=},{index+1=},{one_ans=},{used=}")
            self.permute_rec_memo(nums, index + 1, one_ans, used)
            # 这里回溯要把原先的数组也变回以前的
            #  回溯这部分可以看作是对称的
            one_ans.pop()
            used[i] = False
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
