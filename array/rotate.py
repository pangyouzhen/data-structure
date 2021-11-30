class Solution:
    def rotate(self, nums, k):
        for i in range(0, k):
            nums.insert(0, nums[-1])
            nums.pop(-1)
        return nums


if __name__ == '__main__':
    sol = Solution()
    # nums = [1, 2, 3, 4, 5, 6, 7]
    nums = [-1, -100, 3, 99]
    k = 3
    res = sol.rotate(nums, k)
    print(res)
