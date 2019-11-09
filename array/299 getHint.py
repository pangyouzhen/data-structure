from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = []
        for i in zip(secret, guess):
            if i[0] == i[1]:
                A.append(i)
        all_ = Counter(secret) & Counter(guess)
        B = sum(all_.values()) - len(A)
        return "{}A{}B".format(len(A), B)


if __name__ == '__main__':
    sol = Solution()
    assert sol.getHint("1807", "7810") == "1A3B"
    assert sol.getHint("1123", "0111") == "1A1B"
