class Solution:
    def finalString(self, s: str) -> str:
        a = []
        for i in s:
            if i == "i":
                a = a[::-1]
            else:
                a.append(i)
        return "".join(a)