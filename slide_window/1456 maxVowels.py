from pysnooper import snoop


class Solution:
    # 定长的滑动窗口
    def maxVowels(self, s: str, k: int) -> int:
        # 思路想到了但是索引写的不对
        vowels = {'a', 'e', 'i', 'o', 'u'}
        cnt = 0
        for i in range(k):
            #  range(k): 代表共计k个元素的，索引从0到k-1
            if s[i] in vowels:
                cnt += 1
        res = cnt

        for i in range(k, len(s)):
            #  range(k,l): 代表共计l - k个元素的，索引从k到 l-1
            # 判断首位元素是不是元音字母，如果是滑动窗口的时候要去掉
            if s[i - k] in vowels:
                cnt -= 1
            # 判断末尾元素也就是新进来的元素是不是元音字母，如果是增加1
            if s[i] in vowels:
                cnt += 1
            res = max(res, cnt)
        return res

    # 暴力解法-暴力解法会超时，但是暴力解法相比较滑动窗口，剪枝了重复计算
    # 比如 abcdef 中，k =3时，abc每个字母都得判断是不是元音字母，移动到下一个时候
    # bcd中的bc还得判断是否时元音字母
    @snoop()
    def maxVowels_(self, s: str, k: int) -> int:
        l = len(s)
        # 为什么这里是l-k+1, 因为滑动窗口最后k-1个是没法计算的，那么总的元素是l -(k-1) 为l-k+1个元素
        all_words = [s[i:i + k] for i in range(l - k + 1)]
        max_value = 0
        for i in all_words:
            t = 0
            for j in i:
                if j in "aeiou":
                    t += 1
            if t > max_value:
                max_value = t
        return max_value


if __name__ == '__main__':
    s = "abciiidef"
    k = 3
    sol = Solution()
    print(sol.maxVowels_(s, k))
