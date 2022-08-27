from typing import List
import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paras = re.split("\W+", paragraph)
        paras = [para.lower() for para in paras if para]
        paras_counter = Counter(paras)
        for i, v in paras_counter.most_common(n=len(paras_counter)):
            if i not in banned:
                return i


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    sol = Solution()
    print(sol.mostCommonWord(paragraph, banned))
