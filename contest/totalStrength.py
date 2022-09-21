from typing import List


# TODO timeOut
class Solution:
    # 滑动窗口-get
    # 单调栈？
    def totalStrength(self, strength: List) -> int:
        resuslt = 0
        for i in range(1, len(strength) + 1):
            for j in self.window(strength, i):
                resuslt += min(j) * sum(j)
        return resuslt % (10 ** 9 + 7)

    def window(self, strength: List[int], k) -> List[int]:
        res = []
        for i in range(len(strength) - k + 1):
            # print(strength[i:i+k])
            res.append(strength[i:i + k])
        return res


if __name__ == "__main__":
    func = Solution().totalStrength
    func2 = Solution().window
    nums = [1, 3, 1, 2]
    # print(func(nums))
    print(func(nums))
