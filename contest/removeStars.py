class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for i in s:
            if i == "*":
                del res[-1]
            else:
                res.append(i)
        return ''.join(res)
