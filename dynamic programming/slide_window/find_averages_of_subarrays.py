class Solution:
    # https://zhuanlan.zhihu.com/p/157728782
    def find_averages_of_subarrays(self, s, K):
        if len(s) < 5:
            return False
        right = 4
        res = []
        left = 0
        while right < len(s):
            sum_ = sum(s[left:right]) / K
            res.append(sum_)
            left += 1
            right += 1
        return res

    def find_averages_of_subarrays2(self, s, K):
        if len(s) < 5:
            return False
        right = 4
        res = []
        left = 0
        while right < len(s):
            sum_ = sum(s[left:right]) / K
            res.append(sum_)
            left += 1
            right += 1
        return res


if __name__ == '__main__':
    nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    # 请找出一个数组中所有大小为K的连续子数组的平均值
    K = 5
    sol = Solution()
    print(sol.find_averages_of_subarrays(nums, K))
