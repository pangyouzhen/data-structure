class Solution:
    def thirdMax(self, nums):
        if len(set(nums)) >= 3:
            return list(sorted(set(nums)))[-3]
        else:
            return max(set(nums))


if __name__ == '__main__':
    sol = Solution()
    res = sol.thirdMax([2, 2, 3, 1])
    print(res)
