import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-i for i in gifts]
        heapq.heapify(gifts)
        while k:
            val = heapq.heappop(gifts)
            heapq.heappush(gifts,-int(sqrt(-val)))
            k -= 1
        return -sum(gifts)