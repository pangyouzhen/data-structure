from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        list1 = list(s)
        list2 = indices
        zipped = zip(list1, list2)
        zipped = list(zipped)
        res = sorted(zipped, key=lambda x: x[1])
        result = [i[0] for i in res]
        return "".join(result)


if __name__ == '__main__':
    s = "codeleet"
    indices = [4, 5, 6, 7, 0, 2, 1, 3]
    sol = Solution()
    print(sol.restoreString(s, indices))
