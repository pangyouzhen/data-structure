
class Solution:
    # 应该是贪婪算法+队列
    # TODO
    def splitString(self, s: str) -> bool:
        s = s.lstrip("0")
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                init_val = s[i:j]
                print(init_val)
                t = s[j:]
                while t:
                    print(init_val)
                    t = t.lstrip("0")
                    _ = int(init_val) - 1
                    temp = str(_)
                    if temp == t[:len(temp)]:
                        t = t.lstrip(temp)
                        init_val = int(temp)
                    else:
                        break
                if not t:
                    return True
        return False


if __name__ == '__main__':
    s = "10009998"
    func = Solution().splitString
    # assert func(s) is True
    assert func("1234") is False
    # assert func("050043") is True
