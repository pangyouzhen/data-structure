from typing import List

# TODO
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        for i in range(2,target/2 + 1):
            q,r = divmod(target * 2,i)
            # 偶数形式
            if r == 0:
                pass