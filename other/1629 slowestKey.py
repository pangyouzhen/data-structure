from typing import List


class Solution():
    def slowestKey(self, releaseTimes: List, keysPressed: str) -> str:
        max_val = 0
        last = 0
        last_char = None
        for i, v in zip(releaseTimes, keysPressed):
            if (i-last) > max_val:
                max_val = i - last
                last_char = v
            elif (i-last) == max_val:
                if v > last_char:
                    last_char = v
            last = i
        return last_char


if __name__ == "__main__":
    func = Solution().slowestKey
    releaseTimes = [9,29,49,50]
    keysPressed = "cbcd"
    print(func(releaseTimes,keysPressed))
