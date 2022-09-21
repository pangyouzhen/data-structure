from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        one_ans = []
        self.permute_memo(nums, one_ans)
        return self.res

    def permute_memo(self, nums, one_ans):
        if len(one_ans) == len(nums):
            self.res.append(one_ans[:])
            return
        for i in nums:
            if i in one_ans:
                continue
            one_ans.append(i)
            self.permute_memo(nums,one_ans)
            one_ans.pop(-1)

if __name__ == '__main__':
    func = Solution().permute
    nums = [1,2,3]
    print(func(nums))