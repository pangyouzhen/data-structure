import bisect
from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        all_prime = [i for i in range(2, 1000) if self.is_prime(int(i))]
        t = nums[::-1]
        print(all_prime)
        for i in range(1, len(t)):
            if t[i - 1] - t[i] > 0:
                continue
            else:
                v = t[i - 1] - t[i]
                # 找到大于3 v，小于9 t[i]之间的质数
                l = bisect.bisect_right(all_prime, v)
                r = bisect.bisect_left(all_prime, t[i])
                # 如果没有就return
                if l > r:
                    return False
                else:
                    # 找到第一个符合递增的数字
                    find = False
                    for j in all_prime[l:r]:
                        if t[i] - j < t[i - 1]:
                            t[i] = t[i] - j
                            find = True
                            break
                    if not find:
                        return False
        # print(t)
        return True

    def is_prime(self, num):
        for j in range(2, int(num**0.5) + 1):
            if num % j == 0:
                return False
        return True


if __name__ == "__main__":
    func = Solution().primeSubOperation
    nums = [4,9,6,10]
    print(func(nums))
