from typing import List


#  这个使用的是DP不是其他思想哈
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        result = 0
        # 其实就是将原先的数组分为连续的几组,使用栈来解决
        res = s[0]
        m = [0]
        for i, v in enumerate(s[1:]):
            print(m)
            if v == res:
                m.append(i + 1)
            else:
                if len(m) > 1:
                    val = min(m)
                    result += val
                else:
                    res = v
                    m = [i + 1]
        return result


if __name__ == '__main__':
    # s = "abaac"
    # cost = [1, 2, 3, 4, 5]
    # s = "aabaa"
    # cost = [1, 2, 3, 4, 1]
    s = "aaabbbabbbb"
    # 3+5 + 3+ 5+ 4 + 5+1
    cost = [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]
    sol = Solution()
    print(sol.minCost(s, cost))
