from typing import List
from copy import deepcopy

# TODO
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        res = []
        for i in range(0, n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    res.append((i, j, k))
        print(res)
        c = 0
        for i, j, k in res:
            a = 0
            b = 0
            i_copy = deepcopy(i)
            j_copy = deepcopy(j)
            k_copy = deepcopy(k)
            while i_copy < j_copy:
                a = arr[i_copy] ^ a
                i_copy += 1
            while j_copy <= k_copy:
                b = arr[j_copy] ^ b
                j_copy += 1
            if a == b:
                # print(i, j, k)
                c += 1
        return c


if __name__ == '__main__':
    arr = [2, 3, 1, 6, 7]
    # arr = [1, 1, 1, 1, 1]
    # timeout
    # arr = [808, 874, 66, 212, 150, 827, 941, 951, 26, 906, 912, 332, 732, 319, 995, 119, 916, 890, 238, 385, 367, 806,
    #        585, 451, 906, 699, 305, 476, 237, 823, 986, 794, 192, 237, 45, 671, 690, 100, 726, 936, 382, 610, 796, 674,
    #        446, 486, 88, 433, 489, 319, 214, 117, 163, 148, 55, 735, 744, 92, 692, 611, 215, 519, 720, 620, 188, 477,
    #        353, 6, 359, 896, 743, 490, 781, 743, 490, 9, 483, 815, 716, 71, 651, 65, 714, 207, 517, 124, 633, 623, 22,
    #        768, 790, 296, 574, 289, 799, 186, 933, 514, 423, 301, 138, 99, 233, 910, 871, 48, 855, 532, 323, 168, 491,
    #        914, 633, 124, 517, 258, 775, 326, 577, 127, 574, 770, 316, 835, 639, 828, 323, 177, 498, 366, 156, 644, 536,
    #        920, 384, 133, 261, 181, 432, 951, 519, 903, 384, 93, 477, 400, 77, 647, 714, 645, 79, 451, 396, 959, 563,
    #        332, 895, 81, 814, 31, 817, 702, 399]
    sol = Solution()
    print(sol.countTriplets(arr))
