class Solution:
    def decodeString(self, s: str) -> str:
        t = []
        for i in s:
            if i == "]":
                start = t[::-1].index("[")
                char_ = t[::-1][0:start]
                print(f"{char_ = }")
                num = t[::-1][start+1]
                print(f"{num = }")
                m = int(num) * char_
                print(f"{t = }")
                print(f"{m = }")
##                t.remove()
                t.extend(m[::-1])
            else:
                t.append(i)
        return "".join(t)

if __name__ == "__main__":
    sol = Solution()
    print(sol.decodeString("3[a]2[bc]"))
