from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # 使用dfs转成字典都要  n^2的形式
        if len(nums) < 2:
            return []
        if len(nums) == 2 and nums[1] - nums[0]:
            return []
        global result
        result = []
        # 是树，还是图，不平衡的树，[6,7] 不是初始节点变了，而是第一层的[4,6,7,7] 进行遍历
        self.findSubsequences_memo(nums, 0, [],[False] * len(nums))
        return result

    def findSubsequences_memo(self, nums: List[int], index, one_ans, used):
        # 结束条件 需要修改
        if index >= len(nums):
            result.append(one_ans[:])
            return
        for i, v in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            one_ans.append(nums[i])
            self.findSubsequences_memo(nums[i:], index + 1 + i, one_ans, used)
            one_ans.pop()
            used[i] = False
        return


if __name__ == '__main__':
    sol = Solution()
    a = sol.findSubsequences([4, 6, 7, 7])
    # print(len(a))
    print(a)