class Solution:
# TODO  check !!! this is tree & time is n^2
    def lis(self, ls):
        # this is a tree
        res = []
        for i in range(0, len(ls)):
            if i == 0:
                res.append([ls[0]])
            elif ls[i] < ls[i - 1]:
                res.append([ls[i]])
            else:
                len_res = len(res)
                # print(len_res)
                # print("--------")
                for t in range(1, len_res + 1):
                    if ls[i] > res[-t][-1]:
                        res[-t].append(ls[i])
                # [len_res.items()]
                # pass
            res = sorted(res, key=len)
        return len(res[-1])
        # return max(list(map(len, res)))


#     sorted(b,key=len)


if __name__ == '__main__':
    sol = Solution()
    # [3,] = [3,]
    assert sol.lis([3]) == 1
    # [3, 10,] = [3, 10,]
    assert sol.lis([3, 10, ]) == 2
    # [3, 10, 2,] = [3, 10,]
    assert sol.lis([3, 10, 2, ]) == 2
    # [3, 10, 2, 1] = [3, 10]
    assert sol.lis([3, 10, 2, 1]) == 2
    # [3, 10, 2, 1, 20] = [3, 10, 20]
    assert sol.lis([3, 10, 2, 1, 20]) == 3
    #    M[i+1] =  M[i] + if(m[i] > m[i-1])
    # [4,] = [4,]
    assert sol.lis([4]) == 1
    # [4, 5] = [4, 5,]
    assert sol.lis([4, 5, ]) == 2
    # [4, 5, 1,] = [4, 5]
    assert sol.lis([4, 5, 1, ]) == 2
    # [4, 5, 1, 2] = [4, 5,] /// [1,2]
    assert sol.lis([4, 5, 1, 2]) == 2
    # [4, 5, 1, 2, 3] = [1, 2, 3]
    assert sol.lis([4, 5, 1, 2, 3]) == 3

    #     [50, 3]  = [3,] / [50]
    assert sol.lis([50, 3, ]) == 1
    #     [50, 3, 10,]  = [3, 10]
    assert sol.lis([50, 3, 10, 7, ]) == 2
    #     [50, 3, 10, 7, 40]  = [3, 7, 40]
    assert sol.lis([50, 3, 10, 7, 40]) == 3
    #     [50, 3, 10, 7, 40, 80]  = [3, 7, 40, 80]
    assert sol.lis([50, 3, 10, 7, 40, 80]) == 4