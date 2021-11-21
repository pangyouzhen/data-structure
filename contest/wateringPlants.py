from typing import List
from copy import deepcopy

# from pysnooper import snoop


class Solution:
    # @snoop()
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res = 0
        _ = deepcopy(capacity)
        for i, v in enumerate(plants):
            if capacity >= v:
                res += 1
            else:
                res += i
                res += (i + 1)
                capacity = _
            capacity = capacity - v
        return res


if __name__ == '__main__':
    func = Solution().wateringPlants
    # plants = [2, 2, 3, 3]
    # plants = [2, 2]
    # capacity = 5
    # plants = [1, 1, 1, 4, 2, 3]
    # capacity = 4
    plants = [3, 2, 4, 2, 1]
    capacity = 6
    print(func(plants, capacity))
