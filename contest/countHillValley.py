from typing import List


class Solution:
    def countHillValley(self, nums: List) -> int:
        res = 0
        ns = []
        pre = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == pre:
                continue
            else:
                ns.append(pre)
                pre = nums[i]
        ns.append(pre)
        if len(ns) <= 2:
            return 0
        for i in range(1, len(ns) - 1):
            if ns[i] > ns[i - 1] and ns[i] > ns[i + 1]:
                res += 1
            elif ns[i] < ns[i - 1] and ns[i] < ns[i + 1]:
                res += 1
        return res


if __name__ == "__main__":
    func = Solution().countHillValley
    nums = [6, 6, 5, 5, 4, 1]
    print(func(nums))
