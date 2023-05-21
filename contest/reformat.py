from itertools import chain


class Solution:
    def reformat(self, s: str) -> str:
        alphas, nums = [], []
        for i in s:
            if i.isdigit():
                nums.append(i)
            elif i.isalpha():
                alphas.append(i)
        if abs(len(alphas) - len(nums)) > 1:
            return ""
        if len(alphas) > len(nums):
            return alphas[0] + "".join(chain.from_iterable(list(zip(nums, alphas[1:]))))
        elif len(nums) > len(alphas):
            return nums[0] + "".join(chain.from_iterable(list(zip(alphas, nums[1:]))))
        else:
            return ''.join(chain.from_iterable(list(zip(alphas, nums))))


if __name__ == '__main__':
    func = Solution().reformat
    s = "covid2019"
    print(func(s))
