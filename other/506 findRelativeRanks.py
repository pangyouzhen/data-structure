
from typing import List


class Solution:
    desc = ("Gold Medal", "Silver Medal", "Bronze Medal")

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = [""] * len(score)
        arr = sorted(enumerate(score), key=lambda x: -x[1])
        for i, (idx, _) in enumerate(arr):
            ans[idx] = self.desc[i] if i < 3 else str(i + 1)
        return ans


if __name__ == "__main__":
    func = Solution().findRelativeRanks
    score = [5, 4, 3, 2, 1]
    print(func(score))
