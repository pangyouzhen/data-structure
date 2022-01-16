from typing import List


class Solution():
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        l = len(s)
        group = l / k
        if int(group) == group:
            group = group
        else:
            group += 1
        res = []
        for i in range(int(group)):
            res.append(s[i*k:(i+1)*k])
        if len(res[-1]) != k:
            res[-1] = res[-1] + (k - len(res[-1])) * fill
        return res


if __name__ == "__main__":
    func = Solution().divideString
    nums = []
    print(func(nums))
