class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            a = []
            for i in range(0,len(s),k):
                i_val = 0
                for j in s[i:i+k]:
                    i_val += int(j)
                a.append(str(i_val))
            s = "".join(a)
        return s

if __name__ == "__main__":
    func = Solution().digitSum
    s = "11111222223"
    k = 3
    print(func(s,k))