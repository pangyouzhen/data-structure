from collections import Counter


class Solution:
    def largestPalindromic(self, num: str) -> str:
        d = Counter(num)
        odd = []
        even = []
        for k, v in d.items():
            if v % 2 == 0:
                tmp = [k] * int((v/2))
                even.extend(tmp)
            else:
                if v // 2 > 0:
                    tmp = [k]  * int((v / 2))
                    even.extend(tmp)
                odd.append(k)
        fst_odd = []
        if odd:
            odd.sort(reverse=True)
            fst_odd.append(odd[0])
        if even:
            even.sort(reverse=True)
        if set(even) == {'0'}:
            if not fst_odd:
                return '0'
            even = []
        res = []
        res.extend(even)
        res.extend(fst_odd)
        res.extend(even[::-1])
        res = [str(i) for i in res]
        return ''.join(res)


if __name__ == "__main__":
    # num = "444947137"
    num = "00009"
    func = Solution().largestPalindromic
    print(func(num))
