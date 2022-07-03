from string import ascii_lowercase

from black import main


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        a = key.replace(" ", "")
        print(a)
        d = {}
        k_pointer = 0
        m_pointer = 0
        while k_pointer < len(a):
            i = a[k_pointer]
            if i not in d.keys():
                d[i] = ascii_lowercase[m_pointer]
                k_pointer += 1
                m_pointer += 1
            else:
                k_pointer += 1
        res = []
        for i in message:
            if i.isalpha():
                res.append(d[i])
            else:
                res.append(" ")
        return "".join(res)


if __name__ == "__main__":
    func = Solution().decodeMessage
    key = "the quick brown fox jumps over the lazy dog"
    message = "vkbs bs t suepuv"
    print(func(key, message))
