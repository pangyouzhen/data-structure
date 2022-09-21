from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        a, j = [], 0
        for x in pushed:
            a.append(x)
            while a and a[-1] == popped[j]:
                a.pop()
                j += 1
        return len(a) == 0


if __name__ == '__main__':
    func = Solution().validateStackSequences
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    pushed1 = [1, 2, 3, 4, 5]
    popped1 = [4, 5, 3, 2, 1]
    print(func(pushed1, popped1))
