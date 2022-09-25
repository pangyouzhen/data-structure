from collections import Counter


class Solution:
    def largestInteger(self, num: int) -> int:
        s = str(num)
        c = Counter(s)
        k = c.keys()
        res = []
        for i, v in enumerate(s):
            if int(v) % 2 == 0:
                for j in ["8", '6', '4', '2', '0']:
                    if j in k and c[j] != 0:
                        res.append(j)
                        c[j] -= 1
                        break
            else:
                for j in ["9", '7', '5', '3', '1']:
                    if j in k and c[j] != 0:
                        res.append(j)
                        c[j] -= 1
                        break

        return int(''.join(res))


if __name__ == "__main__":
    func = Solution().largestInteger
