
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        continue_one_nums = 0
        continue_zero_nums = 0
        last_val = None
        last_val_nums = 0
        for i in s:
            if i != last_val:
                last_val_nums = 1
                last_val = i
            else:
                last_val_nums += 1
            if i == "1":
                continue_one_nums = max(continue_one_nums,last_val_nums)
            else:
                continue_zero_nums = max(continue_zero_nums,last_val_nums)
        if continue_one_nums > continue_zero_nums:
            return True
        return False

if __name__ == '__main__':
    func = Solution().checkZeroOnes
    s = "1101"
    print(func(s))