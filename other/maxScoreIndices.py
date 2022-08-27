from typing import List


class Solution:
    def maxScoreIndices(self, nums: List) -> List[int]:
        zeros = 0
        ones = nums.count(1)
        scores = []
        scores.append(ones)
        l = len(nums)
        for i in range(l):
            if nums[i] == 0:
                zeros += 1
            if nums[i] == 1:
                ones -= 1
            scores.append(zeros + ones)
        max_val = max(scores)
        print(scores)
        res = []
        for i,v in enumerate(scores):
            if v == max_val:
                res.append(i)
        return res

if __name__ == "__main__":
    func = Solution().maxScoreIndices
    nums = [0,0,1,0]
    print(func(nums))
