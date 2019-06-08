# https://www.cnblogs.com/Lin-Yi/p/7309143.html

class Solution:
    # def half(self, nums):
    #     t = int(len(nums) / 2) + 1
    #     return nums[:t], nums[t:]

    # 本来想得是for循环使用memo = [None] * (len(left) + len(right))
    def merge(self, left, right):
        memo = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                memo.append(left[0])
                left.pop(0)
            else:
                memo.append(right[0])
                right.pop(0)
        memo += left
        memo += right
        return memo

    def merge_sort(self, nums):
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        ll = self.merge_sort(left)
        rl = self.merge_sort(right)

        return self.merge(ll, rl)


if __name__ == '__main__':
    sol = Solution()
    nums = [38, 27, 43, 3, 9, 82, 10]
    res = sol.merge_sort(nums)
    print(res)
    # left, right = sol.half(nums)
    # left1 = [27, 38]
    # right1 = [3, 43]
    # print(sol.merge(left1, right1))
