from typing import List


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        a = []
        t = []
        for i in range(len(nums)):
            if nums[i] % k == 0:
                t.append(nums[i])
            else:
                a.append(t)
                t = []
        a.append(t)
        print(a)
        res = []
        for j in a:
            if j and k in j:
                res.append(j)


if __name__ == '__main__':
    # nums = [9, 3, 1, 2, 6, 3]
    nums = [9, 3, 6, 3]
    k = 3
    func = Solution().subarrayGCD
    print(func(nums, k))
