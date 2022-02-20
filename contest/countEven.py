class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for i in range(1, num + 1):
            str_i = list(str(i))
            int_i = [int(j) for j in str_i]
            if sum(int_i) % 2 == 0:
                res += 1
        return res


if __name__ == '__main__':
    pass
