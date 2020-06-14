class Solution:
    #  主要疑问点是，双指针只能指向两个数字，另外一个数字是怎样获取的
    #  关键是为什么使用双指针，两数之和用的是双指针，所以
    def threeSum(self, nums):
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n - 2):
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if nums[i] + nums[-2] + nums[-1] < 0:
                continue
            if 0 < i and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l + 1 < r and nums[l] == nums[l + 1]:
                        l = l + 1
                    while l < r - 1 and nums[r] == nums[r - 1]:
                        r = r - 1
                    l = l + 1
                    r = r - 1
                elif tmp < 0:
                    l = l + 1
                else:
                    r = r - 1
        return res

    def three_sum(self, nums):
        nums.sort()
        result = []
        for k in range(0, len(nums) - 2):
            #  这个if 是判断重复的情况，最后写
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            target = -nums[k]
            i = k + 1
            j = len(nums) - 1
            while i < j:
                print(f"{k},,{i},,{j}")
                sum_ = nums[i] + nums[j]
                if sum_ == target:
                    set_ = [nums[k], nums[i], nums[j]]
                    result.append(set_)
                    i += 1
                    #  这个while是判断重复的情况，最后写
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    j -= 1
                    #  这个while是判断重复的情况，最后写
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif sum_ < target:
                    i += 1
                else:
                    j -= 1
        return result


if __name__ == '__main__':
    sol = Solution()
    res = sol.three_sum([-1, 0, 1, 2, -1, -4])
    print(res)
