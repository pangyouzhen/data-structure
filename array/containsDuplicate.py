class Solution:
    def containsDuplicate(self, nums):
        if sorted(list(set(nums))) == sorted(nums):
            return False
        else:
            return True


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 5, -2, -4, 0]
    res = sol.containsDuplicate(nums)
    print(res)
