from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        latitude_list = [0] * (len(gain) + 1)
        for i in range(1, len(gain) + 1):
            latitude_list[i] = latitude_list[i - 1] + gain[i - 1]
        return max(latitude_list)


if __name__ == '__main__':
    gain = [-5, 1, 5, 0, -7]
    sol = Solution()
    print(sol.largestAltitude(gain))
