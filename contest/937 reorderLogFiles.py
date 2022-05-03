from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def trans(log: str) -> tuple:
            a, b = log.split(" ", 1)
            return (0, b, a) if b[0].isalpha() else (1,)

        logs.sort(key=trans)  # sort 是稳定排序
        return logs


if __name__ == "__main__":
    logs = [
        "dig1 8 1 5 1",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero",
    ]
    logs2 = [
        "a1 9 2 3 1",
        "g1 act car",
        "zo4 4 7",
        "ab1 off key dog",
        "a8 act zoo",
        "g2 act car",
    ]
    func = Solution().reorderLogFiles
    print(func(logs2))
