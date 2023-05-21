from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        all_ans = []
        one_ans = []

        def permute_memo(nums, one_ans):
            if len(one_ans) == len(nums):
                all_ans.append(one_ans[:])
            for i in nums:
                if i in one_ans:
                    continue
                one_ans.append(i)
                permute_memo(nums, one_ans)
                one_ans.pop()

        permute_memo(nums, one_ans)
        return all_ans


if __name__ == '__main__':
    func = Solution().permute
    nums = [1, 2, 3]
    print(func(nums))
