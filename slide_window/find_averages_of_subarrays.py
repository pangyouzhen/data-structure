class Solution:
    # https://zhuanlan.zhihu.com/p/157728782
    def find_averages_of_subarrays(self, s, K):
        if len(s) < 5:
            return False

        val = sum(s[0:K]) / K
        res = [val]
        for i in range(K, len(s)):
            val += s[i] / K - s[i - K] / K
            res.append(float(format(val, '.1f')))
        return res


if __name__ == '__main__':
    nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    # 请找出一个数组中所有大小为K的连续子数组的平均值
    K = 5
    sol = Solution()
    print(sol.find_averages_of_subarrays(nums, K))
