class Solution:
    def singleNumber(self, nums):
        a = 0
        t = []
        while (a < len(nums)):
            if nums[a] not in t:
                t.append(nums[a])
            else:
                t.remove(nums[a])
            a = a + 1
        return t[0]


if __name__ == '__main__':
    sol = Solution()
    res = sol.singleNumber([2, 1, 2])
    print(res)
