class Solution:
    def findComplement(self, num: int) -> int:
        num_bin = bin(num)[2:]
        complement = []
        for i in num_bin:
            temp = 1 - int(i)
            complement.append(str(temp))
        res = ''.join(complement)
        return int(res, base=2)
