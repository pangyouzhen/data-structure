from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        s_dict = {"R": [0, 1],
                  "L": [0, -1],
                  "U": [-1, 0],
                  "D": [1, 0]}
        res = []
        for j in range(len(s)):
            pos = [startPos[0], startPos[1]]
            t = 0
            for i in s[j:]:
                pos[0] = pos[0] + s_dict[i][0]
                pos[1] = pos[1] + s_dict[i][1]
                if pos[0] >= n or pos[1] >= n or pos[0] < 0 or pos[1] < 0:
                    break
                else:
                    t += 1
            res.append(t)
        return res



if __name__ == '__main__':
    func = Solution().executeInstructions
    n = 3
    startPos = [0, 1]
    s = "RRDDLU"
    print(func(n, startPos, s))
