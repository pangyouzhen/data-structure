class Solution:
    # TODO
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        val = (query_row + 2) * (query_row + 1)
        if val <= poured:
            return 1
        else:
            last = (query_row + 1) * query_row
            if last >= poured:
                return 0
            else:
                every = (poured - last) / (query_row + 1)
                if query_glass == (query_row + 1) or query_glass == 0:
                    return every / 2
                return every


if __name__ == "__main__":
    func = Solution().champagneTower
    p = 2
    qc = 1
    qr = 1
    print(func(p, qc, qr))
