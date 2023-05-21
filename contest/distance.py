from typing import List
from collections import defaultdict


# class Solution:
#     def distance(self, nums: List[int]) -> List[int]:
#         d = defaultdict(list)
#         for i, v in enumerate(nums):
#             d[v].append(i)
#         print(d)
#         for i, v in enumerate(nums):
#             l = d[v]

def get_values(v: List[int]):
    S = []
    s0 = 0
    for i in range(len(v)):
        s0 += abs(v[0] - v[i])
    S.append(s0)
    for i in range(0, len(v) - 1):
        S.append(S[i] + (2 * i + 1 - (len(v)-1)) * (v[i + 1] - v[i]))
    return S

if __name__ == "__main__":
    a = [0,2,4,5,6,8]
    print(get_values(a))