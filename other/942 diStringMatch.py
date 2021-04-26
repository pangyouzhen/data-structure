from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        minnum, maxnum = 0, len(S)
        ans = []
        for i in S:
            if i == 'I':
                ans.append(minnum)
                minnum += 1
            else:
                ans.append(maxnum)
                maxnum -= 1
        ans.append(minnum)
        return ans


if __name__ == '__main__':
    s = "DDI"
    sol = Solution()
    print(sol.diStringMatch(s))
