from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        nh = zip(names, heights)
        nhs = sorted(nh, key=lambda x: x[1], reverse=True)
        return [i[0] for i in nhs]


if __name__ == '__main__':
    func = Solution().sortPeople
    names = ["Mary", "John", "Emma"]
    heights = [180, 165, 170]
    print(func(names, heights))
