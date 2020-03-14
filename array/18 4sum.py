from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        for i in range(0, len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                p = j + 1
                q = len(nums) - 1
                current_target = target - nums[i] - nums[j]
                while p < q:
                    sum_ = nums[p] + nums[q]
                    if sum_ == current_target:
                        res.append([nums[i], nums[j], nums[p], nums[q]])
                        p += 1
                        while p < q and nums[p] == nums[p - 1]:
                            p += 1
                        q -= 1
                        while p < q and nums[q] == nums[q + 1]:
                            q -= 1
                    elif sum_ < current_target:
                        p += 1
                    else:
                        q -= 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.fourSum([-3, -1, 0, 2, 4, 5], 0))
