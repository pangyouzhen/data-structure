from typing import List


class Solution:
    # 定长的滑动窗口
    # https://zhuanlan.zhihu.com/p/157728782
    def find_averages_of_subarrays(self, s: List[int], K: int):
        if len(s) < K:
            return False

        val = sum(s[0:K]) / K
        res = [val]
        for i in range(K, len(s)):
            # 队列元素是i-K,新增的元素是i
            val += s[i] / K - s[i - K] / K
            res.append(float(format(val, '.1f')))
        return res

    def find_averages_of_subarrays_(self, s: List[int], K: int):
        # 最后K-1 个元素是没法计算的,所以总长度为 l -(K-1)
        vals = [s[i:i + K] for i in range(len(s) - K + 1)]
        return [sum(i) / K for i in vals]


if __name__ == '__main__':
    nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    # 请找出一个数组中所有大小为K的连续子数组的平均值
    K = 5
    sol = Solution()
    print(sol.find_averages_of_subarrays(nums, K))
    print(sol.find_averages_of_subarrays_(nums, K))
