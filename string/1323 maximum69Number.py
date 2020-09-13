class Solution:
    def maximum69Number(self, num: int) -> int:
        nums_str = list(str(num))
        for i in range(len(nums_str)):
            if nums_str[i] == "6":
                nums_str[i] = "9"
                break
        return int("".join(nums_str))


if __name__ == '__main__':
    num = 9669
    sol = Solution()
    print(sol.maximum69Number(num))
