import datetime
from typing import List
import time


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:

        x1 = event1[-1]
        y1 = event2[-1]
        x = event1[0]
        y = event2[0]
        x = time.strptime(x, "%H:%M")
        y = time.strptime(y, "%H:%M")
        y1 = time.strptime(y1, "%H:%M")
        x1 = time.strptime(x1, "%H:%M")

        if y >= x and y <= x1:
            return True
        elif y <= x <= y1:
            return True
        elif x <= y <= x1:
            return True
        return False


if __name__ == '__main__':
    func = Solution().haveConflict
    event1 = ["01:00", "02:00"]
    event2 = ["01:20", "03:00"]
    event11 = ["16:53", "19:00"]
    event22 = ["10:33", "18:15"]
    print(func(event1, event2))
    assert func(event11, event22) is True
    event111 = ["01:00", "02:00"]
    event222 = ["01:20", "03:00"]
    assert func(event111, event222) is True
    event1111 = ["14:13", "22:08"]
    event2222 = ["02:40", "08:08"]
    assert func(event1111, event2222) is False
