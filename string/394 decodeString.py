import re


class Solution:
    def decodeString(self, s: str) -> str:
        pattern = re.compile("(\d+)\[(\w+)\]")
        m = pattern.findall(s)
        while m:
            for num, char in m:
                s = s.replace(f"{num}[{char}", char * int(num))
                m = pattern.findall(s)
        return s


if __name__ == "__main__":
    sol = Solution()
    print(sol.decodeString("3[a]2[bc]"))
