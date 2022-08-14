from itertools import permutations


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in permutations(a, len(pattern)+1):
            # print(''.join(i))
            num = ''.join(i)
            if self.match_pattern(num,pattern):
                return num


    def match_pattern(self,num: str, pattern: str):
        for i in range(1, len(num)):
            if (int(num[i]) - int(num[i-1])) > 0 and pattern[i-1] == 'I':
                continue
            elif (int(num[i]) - int(num[i-1]) < 0) and pattern[i-1] == "D":
                continue
            else:
                return False
        return True


if __name__ == "__main__":
    func = Solution().smallestNumber
    pattern = "IIIDIDDD"
    print(func(pattern))
