# https://www.geeksforgeeks.org/python-program-for-kmp-algorithm-for-pattern-searching-2/
def computerLPSArray(pat, M, lps):
    len_ = 0
    lps[0] = 0
    i = 1
    while i < M:
        if pat[i] == pat[len_]:
            len_ += 1
            lps[i] = len_
            i += 1
        else:
            if len_ != 0:
                len_ = lps[len_ - 1]
            else:
                lps[i] = 0
                i += 1


def kmp_search(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0] * M
    j = 0
    computerLPSArray(pat, M, lps)
    i = 0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            print("pattern found", str(i - j))
            j = lps[j - 1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


if __name__ == '__main__':
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    txt1 = "THIS IS ATEST TEXT"
    pat2 = "TEST1"
    kmp_search(pat, txt)
    kmp_search(pat2, txt1)
    # KMP 算法实现的功能是 "adefe".index("fe")的功能
    # KMP 中，PMT中的值是字符串的前缀集合与后缀集合的交集中最长元素的长度。
    # next 数组将KMP 平移，首位用-1进行填充
    # TODO 有了PMT和next数组之后步骤
    a = "ABABCABAB"
    perfix = set([a[:i] for i in range(1, len(a) - 1)])
    suffix = set([a[:i] for i in range(2, len(a))])
    print("PMT", len(max(set(perfix).intersection(set(suffix)), key=len)))
